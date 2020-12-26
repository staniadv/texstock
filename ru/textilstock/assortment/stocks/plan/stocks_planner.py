import os

import pandas as pd

from ru.textilstock.assortment.stocks.plan.article_count import ArticleCount
from ru.textilstock.assortment.stocks.remains_djama_parser import parse_djama_stocks

from pathlib import Path
this_file_path = Path(__file__).parent.absolute()
article_to_djama_article_mapping = 'article_to_djama_article_mapping.xlsx'


def remove_ouput_files(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def create_article_mappings():
    print(this_file_path)
    article_to_stock_mapping_df = pd.read_excel(str(this_file_path) + '/' + article_to_djama_article_mapping)
    mapping_dict = {}
    for index, row in article_to_stock_mapping_df.iterrows():
        article = row['article']

        if article not in mapping_dict:
            mapping_dict[article] = list()

        mapping_dict[article].append(ArticleCount(row['mapping'], row['count']))
    return mapping_dict


def create_orders(article_plan_src, djama_stocks_file, djama_article_order, article_order):
    article_to_djama_mapping_dict = create_article_mappings()
    article_plan_df = pd.read_excel(article_plan_src)
    djama_stocks_df = parse_djama_stocks(djama_stocks_file)
    djama_stocks_df.set_index('article', inplace=True)

    for index, row in article_plan_df.iterrows():
        article = row['article']
        if article not in article_to_djama_mapping_dict:
            print("WARNING: Article in plan nas no mapping: " + article)
            continue

        djama_articles = article_to_djama_mapping_dict[article]

        djama_articles_cnt_to_order_dict = {}
        for djama_article in djama_articles:
            count_required = row['count'] * djama_article.count

            if djama_article.article not in djama_articles_cnt_to_order_dict:
                djama_articles_cnt_to_order_dict[djama_article.article] = 0

            djama_articles_cnt_to_order_dict[djama_article.article] = djama_articles_cnt_to_order_dict[
                                                                          djama_article.article] + count_required

        article_rejected = False
        for djama_article, count_required in djama_articles_cnt_to_order_dict.items():
            try:
                # проверяем что все строки в наличии
                article_row = djama_stocks_df.loc[djama_article]
                if article_row['count'] < count_required:
                    print("Stocks less then required " + djama_article + ", actual: "
                          + str(article_row['count']) + ", required: " + str(count_required))
                    article_rejected = True
                    break
            except KeyError:
                print("No stocks for " + djama_article)
                article_rejected = True
                break
        if article_rejected:
            print(article + " REJECTED")
            continue

        for djama_article, count_required in djama_articles_cnt_to_order_dict.items():
            article_row = djama_stocks_df.loc[djama_article]
            article_row['count'] = article_row['count'] - count_required
            djama_article_order.append(ArticleCount(djama_article, count_required))

        article_order.append(ArticleCount(row['article'], str(row['count'])))





def generate_orders(article_plan_src, djama_stocks_file, out_xlsx_file):
    #print(article_to_stock_mapping_dict)
    article_order = []
    djama_article_order = []
    create_orders(article_plan_src, djama_stocks_file, djama_article_order, article_order)

    print(djama_article_order)
    print(article_order)
    #TODO обогатить ценами

    #Делаем датасет для Джамы
    djama_article_order_lists = []
    for row in djama_article_order:
        djama_article_order_lists.append([row.article, row.count])
    djama_article_order_df = pd.DataFrame(djama_article_order_lists, columns = ['Артикул', 'Количество'])

    #Складываем дубликаты
    djama_article_order_df = djama_article_order_df.groupby(by=["Артикул"]).sum()
    djama_article_order_df.reset_index()

    #Джойним цены
    djama_prices = pd.read_csv(str(this_file_path) +'/djama_prices.csv')
    djama_article_order_df = pd.merge(djama_article_order_df, djama_prices,
                                      how='left', left_on=['Артикул'],
                                      right_on=['Артикул']
                                      )
    djama_article_order_df['Сумма'] = djama_article_order_df['Цена'] * djama_article_order_df['Количество']

    #Делаем датасет для нас
    article_order_lists = []
    for row in article_order:
        article_order_lists.append([row.article, row.count])
    article_order_df = pd.DataFrame(article_order_lists, columns = ['Артикул', 'Количество'])
    print("Total sum: " + str(djama_article_order_df['Сумма'].sum()))

    #пишем xlsx
    with pd.ExcelWriter('output/' + out_xlsx_file) as writer:
        djama_article_order_df.to_excel(writer, sheet_name='Поставка Джама')
        article_order_df.to_excel(writer, sheet_name='Артикулы для склада')


