import pandas as pd

from ru.textilstock.assortment.djama.xls.order_detalization_parser import parse_order_detalizations

MAPPING_DJAMA_DETAIL_WILD_TO_NOMENCLATURE_FILE_CSV = '/home/stani/PycharmProjects/texstock/ru/textilstock/assortment' \
                                                     '/djama/xls/detail_to_nomen_mapping.csv'

EXCLUDE_BARCODES_FILE = '/home/stani/PycharmProjects/texstock/ru/textilstock/assortment' \
                        '/djama/xls/barcodes_to_exclude.csv'


def join_djama_detail_with_nomen(details_file_csv, nomeclature_file_xlsx):
    order_details_dataset = pd.read_csv(details_file_csv)
    detail_to_nomen_dataset = pd.read_csv(MAPPING_DJAMA_DETAIL_WILD_TO_NOMENCLATURE_FILE_CSV)

    order_details_with_nomenclature = order_details_dataset.join(detail_to_nomen_dataset.set_index('article'),
                                                                 on='article', how='inner')
    wild_nomen_dataset = pd.read_excel(nomeclature_file_xlsx)

    res = order_details_with_nomenclature.join(wild_nomen_dataset.set_index('Артикул поставщика'), on='nomenclature')
    barcodes_to_exclude_df = pd.read_csv(EXCLUDE_BARCODES_FILE)
    barcodes_to_exclude = list(barcodes_to_exclude_df.to_dict()['barcode'].values())

    # filter fields
    res = res[res['nomenclature'].notnull()]
    res = res[res['Баркод'].notnull()]
    res = res[~res['Баркод'].isin(barcodes_to_exclude)]
    # rename fields
    res = res.rename(columns={"nomenclature": "Артикул поставщика", "Розничная цена, руб.": "Розничная цена"})
    res = res.astype({'Баркод': 'int64'})

    res.insert(0, 'cnt', res['count'])
    return res


def write_data_to_csv(data_frame, output_file_csv):
    s = data_frame.to_csv(index=False)
    with open(output_file_csv, "w") as text_file:
        text_file.write(s)


def join_detail_with_nomen_and_write(details_file_csv, nomeclature_file_xlsx, output_file_csv):
    data = join_djama_detail_with_nomen(details_file_csv,
                                        nomeclature_file_xlsx)
    write_data_to_csv(data, output_file_csv)


#
# join_detail_with_nomen_and_write('order_details_tmp.csv',
#                                  '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-01-25T180900.442.xlsx',
#                                  'Output1.csv')


# def j1():
#     order_details = parse_order_detalizations(['1.xls', '2.xls'])
#
#     data = []
#
#     for order in order_details:
#         data.append([order.article, order.count, order.price])
#     df = pd.DataFrame(data=data, columns=['article', 'count', 'price'])
#     join1(df,
#           pd.read_excel('nomen.xlsx'),
#           pd.read_csv(MAPPING_DJAMA_DETAIL_WILD_TO_NOMENCLATURE_FILE_CSV)
#           )
#
#
# def join1(order_details_df, nomeclature_df, detail_to_nomen_df):
#     # print(order_details_df.groupby('article')['count'].sum().to_frame())
#     od = order_details_df.groupby('article')['count'].sum().to_frame()
#
#     order_details_with_nomenclature = od.join(detail_to_nomen_df.set_index('article'),
#                                               on='article', how='inner')
#
#     res = order_details_with_nomenclature.join(nomeclature_df.set_index('Артикул поставщика'), on='nomenclature')
#
#     print(res['count'])
