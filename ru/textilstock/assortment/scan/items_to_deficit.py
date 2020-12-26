import pandas as pd


def get_scan_df(src_barcodes_file, boxes=[]):
    # boxes = list(range(1, 8+1))
    scan_df = pd.read_excel(src_barcodes_file)
    scan_df = scan_df[scan_df['номер короба'].notnull() | scan_df['Баркод'].notnull()]
    if len(boxes) > 0:
        scan_df = scan_df[scan_df['номер короба'].isin(boxes)]
    return scan_df


def items_to_deficit(scan_df, nomen_file, supply_number):
    scan_df = scan_df[scan_df['Баркод'].notnull()]
    scan_df = scan_df.astype({'Баркод': 'int64'})

    scan_groupped = scan_df.groupby(["Баркод"]).size().to_frame('count')
    scan_groupped = scan_groupped.reset_index()

    #nomen_df = pd.read_excel(nomen_file, skiprows=2)
    nomen_df = pd.read_excel(nomen_file)
    nomen_df = nomen_df[nomen_df['Баркод'].notnull()]
    nomen_df = nomen_df[nomen_df['Баркод'].str.isnumeric()]
    nomen_df = nomen_df.astype({'Баркод': 'int64'})

    grp_with_nomen = pd.merge(scan_groupped, nomen_df,
                              how='left', left_on=['Баркод'],
                              right_on=['Баркод']
                              )

    whole_prices_df = pd.read_csv('wholesale_prices.csv')

    grp_with_nomen = pd.merge(grp_with_nomen, whole_prices_df,
                              how='left', left_on=['Артикул ИМТ'],
                              right_on=['article']
                              )

    def_source_df = pd.DataFrame(data=grp_with_nomen, columns=['Бренд', 'Артикул ИМТ', 'Артикул Цвета',
                                                               'Размер', 'Предмет', 'Пол', 'Баркод',
                                                               'count', 'Розничная цена RU',
                                                               'Розничная цена BY', 'Розничная цена KZ',
                                                               'price', 'Валюта', 'базценаопт'])
    def_source_df['count'] = def_source_df['count'] / 2
    def_source_df['Валюта'] = 'руб'
    def_source_df = def_source_df.rename(columns={"count": "Количество", "Артикул поставщика": "артикул",
                                                  "price": "Цена за штуку"})

    def_source_df.to_excel('output/def-source-' + str(supply_number) + '.xlsx', index=False)

    def_by_barcodes = pd.DataFrame(data=grp_with_nomen, columns=['Баркод', 'count'])
    def_by_barcodes['count'] = def_by_barcodes['count'] / 2
    def_by_barcodes = def_by_barcodes.rename(columns={"count": "Количество"})

    def_by_barcodes.to_excel('output/deficit-' + str(supply_number) + '.xlsx', index=False)
