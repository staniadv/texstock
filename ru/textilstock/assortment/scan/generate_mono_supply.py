import pandas as pd

from ru.textilstock.assortment.scan.items_to_deficit import items_to_deficit
from ru.textilstock.assortment.scan.items_to_mix import items_to_mix
import os

from ru.textilstock.assortment.scan.send_mail import send_jrpirnt_files


def get_scan_df(src_barcodes_file, boxes=[]):
    scan_df = pd.read_excel(src_barcodes_file)
    scan_df = scan_df[scan_df['номер короба'].notnull() | scan_df['Баркод'].notnull()]
    if len(boxes) > 0:
        scan_df = scan_df[scan_df['номер короба'].isin(boxes)]
        i = 1
        for boxnum in boxes:
            scan_df['номер короба'] = scan_df['номер короба'].replace([boxnum], i)
            i += 1

    return scan_df


def generate_mono_supply(src_barcodes_file, nomen_file, supply_number, boxes=[]):
    scan_df = get_scan_df(src_barcodes_file, boxes)
    scan_df = scan_df[scan_df['Баркод'].notnull()]
    scan_df = scan_df.astype({'Баркод': 'int64'})
    check_mono_consistency(scan_df)
    scan_groupped = scan_df.groupby(["номер короба", "Баркод"]).size().to_frame('count')
    scan_groupped = scan_groupped.reset_index()

    nomen_df = pd.read_excel(nomen_file, skiprows=2)
    grp_with_nomen = pd.merge(scan_groupped, nomen_df,
                              how='left', left_on=['Баркод'],
                              right_on=['Баркод'])

    grp_with_nomen = pd.DataFrame(data=grp_with_nomen, columns=['номер короба', 'Артикул поставщика', 'count'])
    grp_with_nomen['count'] = grp_with_nomen['count'] / 2

    grp_with_nomen = grp_with_nomen.rename(columns={"Артикул поставщика": "артикул", "count": "Кол-во"})
    grp_with_nomen.to_excel('monofeed1.xlsx', index=False)


def check_mono_consistency(df):
    df_groupped = df.groupby(["номер короба", "Баркод"]).size().to_frame('count')
    box_barcodes_groupped = df_groupped.groupby(["номер короба"]).size().to_frame('count')
    box_barcodes_groupped = box_barcodes_groupped[box_barcodes_groupped['count'] > 1]

    if len(box_barcodes_groupped.index) > 0:
        print(box_barcodes_groupped)
        raise Exception('More than one article in box.')


src_barcodes_file = '/home/stani/Загрузки/штрихи_моно_тест.xlsx'
nomen_file = '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-05-22T223634.988.xlsx'

supply_number = 1103646

generate_mono_supply(src_barcodes_file, nomen_file, supply_number)

# штрихи_моно_2020-05-22.xlsx
