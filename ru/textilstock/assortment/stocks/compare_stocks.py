import pandas as pd

from ru.textilstock.assortment.stocks.remains_djama_parser import parse_djama_stocks

MAPPING_DJAMA_DETAIL_WILD_TO_NOMENCLATURE_FILE_CSV = '/home/stani/PycharmProjects/texstock/ru/textilstock/assortment' \
                                                     '/djama/xls/detail_to_nomen_mapping.csv'


def write_data_to_csv(data_frame, output_file_csv):
    s = data_frame.to_csv(index=False)
    with open(output_file_csv, "w") as text_file:
        text_file.write(s)


def compare_stocks(djama_stocks_xls, wildberries_stocks_xlsx, output_csv):
    djama_remains_df = parse_djama_stocks(djama_stocks_xls)

    remains_to_nomen_dataset = pd.read_csv(MAPPING_DJAMA_DETAIL_WILD_TO_NOMENCLATURE_FILE_CSV)

    skipped = djama_remains_df.join(remains_to_nomen_dataset.set_index('article'),
                                    on='article', how='left')
    skipped = skipped[skipped['nomenclature'].isnull()]
    if len(skipped) > 0:
        print("nomenclature NOT exist in " + MAPPING_DJAMA_DETAIL_WILD_TO_NOMENCLATURE_FILE_CSV)
        print(skipped)

    djama_remain_nomenclatured = djama_remains_df.join(remains_to_nomen_dataset.set_index('article'),
                                                       on='article', how='inner')

    wild_remains_dataset = pd.read_excel(wildberries_stocks_xlsx, skiprows=1)
    stock_compare_df = pd.merge(djama_remain_nomenclatured, wild_remains_dataset,
                                how='outer', left_on=['nomenclature'],
                                right_on=['Артикул поставщика']
                                )
    res = pd.DataFrame(data=stock_compare_df, columns=['article', 'nomenclature', 'count',
                                                       'Артикул поставщика',
                                                       'Подольск', 'Новосибирск', 'Хабаровск', 'Краснодар',
                                                       'Екатеринбург', 'Санкт-Петербург'])

    res['sum_all'] = res.fillna(0)['Подольск'] + res.fillna(0)['Новосибирск'] \
                     + res.fillna(0)['Хабаровск'] + res.fillna(0)['Краснодар'] + \
                     res.fillna(0)['Екатеринбург'] + res.fillna(0)['Санкт-Петербург']

    res = res.rename(columns={"count": "Остаток у Джамы", "article": "Артикул Джамы", "sum_all": "Остаток на складах"})
    res = res[['Артикул Джамы', 'Остаток у Джамы', 'nomenclature', 'Артикул поставщика',
               'Остаток на складах',
               'Подольск', 'Новосибирск', 'Хабаровск',
               'Краснодар', 'Екатеринбург', 'Санкт-Петербург']]

    write_data_to_csv(res, output_csv)


# compare_stocks('djama_stocks.xls',
#                '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-02-17T003842.321.xlsx',
#                'out.csv')
