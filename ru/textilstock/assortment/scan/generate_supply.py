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


def generate_supply(src_barcodes_file, nomen_file, supply_number, boxes=[]):
    scan_df = get_scan_df(src_barcodes_file, boxes)


    # save deficit as deficit-supply_number
    items_to_deficit(scan_df, nomen_file, supply_number)

    # save jr csv as supply_number.csv
    items_to_mix(scan_df, nomen_file, supply_number)

    # save jrprint as supply_number.jrprint
    os.system("java -jar ./jrhello-1.0-SNAPSHOT-jar-with-dependencies.jar " +
              "output/" + str(supply_number) + ".csv " +
              "mix_boxes.jrxml " +
              "output/" + str(supply_number) + ".jrprint")


def generate_single(src_barcodes_file, nomen_file, supply_number):
    generate_supply(src_barcodes_file, nomen_file, supply_number)


def generate_selected(src_barcodes_file, nomen_file, box_sets):
    for supply_number, boxes in box_sets.items():
        generate_supply(src_barcodes_file, nomen_file, supply_number, boxes)


def make_inclusive_intervals(supplynum_to_boxes_sets_intervals):
    supply_boxes_sets = dict()
    for key, value in supplynum_to_boxes_sets_intervals.items():
        supply_boxes_sets[key] = list(range(value[0], value[1] + 1))
    return supply_boxes_sets


src_barcodes_file = '/home/stani/Загрузки/штрихи_2020-05-22 (4).xlsx'
nomen_file = '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-05-22T223634.988.xlsx'

supply_number = 1103646
generate_single(src_barcodes_file, nomen_file, supply_number)


# supplynum_to_boxes_sets_intervals = {123: [1, 9], 124: [10, 18], 125: [19, 27]}
# generate_selected(src_barcodes_file, nomen_file, make_inclusive_intervals(supplynum_to_boxes_sets_intervals))

#Отправить jrxml на почту
#send_jrpirnt_files()
