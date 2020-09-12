import pandas as pd

from ru.textilstock.assortment.scan.items_to_deficit import items_to_deficit
from ru.textilstock.assortment.scan.items_to_mix import items_to_mix
import os

from ru.textilstock.assortment.scan.send_mail import send_jrpirnt_files


current_path = os.path.dirname(os.path.abspath(__file__)) + '/'

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
    remove_ouput_files(current_path + '/output')
    generate_supply(src_barcodes_file, nomen_file, supply_number)


def generate_selected(src_barcodes_file, nomen_file, box_sets):
    remove_ouput_files(current_path + '/output')
    for supply_number, boxes in box_sets.items():
        generate_supply(src_barcodes_file, nomen_file, supply_number, boxes)


def make_inclusive_intervals(supplynum_to_boxes_sets_intervals):
    supply_boxes_sets = dict()
    for key, value in supplynum_to_boxes_sets_intervals.items():
        supply_boxes_sets[key] = list(range(value[0], value[1] + 1))
    return supply_boxes_sets


def remove_ouput_files(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


#src_barcodes_file = '/home/stani/Загрузки/barcode_scan_template_ozon.xlsx'
src_barcodes_file = '/home/stani/Загрузки/barcode_111WB (1).xlsx'
nomen_file = '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-09-02T225436.687.xlsx'

supply_number = 1
generate_single(src_barcodes_file, nomen_file, supply_number)

#supplynum_to_boxes_sets_intervals = {1: [19, 25]}
#supplynum_to_boxes_sets_intervals = {1: [1, 9]}
#generate_selected(src_barcodes_file, nomen_file, make_inclusive_intervals(supplynum_to_boxes_sets_intervals))

# Отправить jrxml на почту
#send_jrpirnt_files()
