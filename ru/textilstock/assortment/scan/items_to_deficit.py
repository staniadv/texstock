import pandas as pd


def get_scan_df(src_barcodes_file, boxes = []):
    #boxes = list(range(1, 8+1))
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

    nomen_df = pd.read_excel(nomen_file, skiprows=2)

    grp_with_nomen = pd.merge(scan_groupped, nomen_df,
                              how='left', left_on=['Баркод'],
                              right_on=['Баркод']
                              )

    whole_prices_df = pd.read_csv('wholesale_prices.csv')

    grp_with_nomen = pd.merge(grp_with_nomen, whole_prices_df,
                              how='left', left_on=['Артикул ИМТ'],
                              right_on=['article']
                              )

    grp_with_nomen = pd.DataFrame(data=grp_with_nomen, columns=['Бренд', 'Артикул ИМТ', 'Артикул Цвета',
                                                                'Размер', 'Предмет', 'Пол',
                                                                'count', 'Розничная цена RU',
                                                                'Розничная цена BY', 'Розничная цена KZ',
                                                                'price', 'Валюта', 'базценаопт'])
    grp_with_nomen['count'] = grp_with_nomen['count'] / 2
    grp_with_nomen['Валюта'] = 'руб'
    grp_with_nomen = grp_with_nomen.rename(columns={"count": "Количество", "Артикул поставщика": "артикул",
                                                    "price": "Цена за штуку"})

    grp_with_nomen.to_excel('output/deficit-' + str(supply_number) + '.xlsx', index=False)

