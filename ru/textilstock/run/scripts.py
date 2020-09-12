import csv

import pandas as pd

from ru.textilstock.assortment.barcodes.generator.multiple_barcodes import gen_and_write_barcodes, \
    calc_repeat_dict_count
from ru.textilstock.assortment.djama.xls.order_detalization_parser import parse_order_detalizations
from ru.textilstock.assortment.mixbox.MixBoxChecker import full_check
from ru.textilstock.assortment.mixbox.MixBoxXlsParser import parse
from ru.textilstock.assortment.mixbox.MixBoxProcessor import prepare_boxes_for_deficit, writeDefBoxesToExcel
from ru.textilstock.assortment.tools.barcodegenerator.barcode_template_generator import generate_barcodes_template, \
    repeat_rows

barcode_csv_file = 'barcodes.csv'

# gen_and_write_barcodes('ExportToEXCELOPENXML - 2020-02-02T022159.922.csv', 'ituma.csv')
#
# barcode_csv_file = 'barcodes.csv'
#Полотенце 150 х210 сиреневый (itu)
# generate_barcodes_template('detail.xls',
#                            '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-04-09T184919.179.xlsx',
#                            barcode_csv_file, 8)

#generate_barcodes_template('/home/stani/Загрузки/детализация заказа ИП Алиев ТР (58Полотенце 150 х210).xls', '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-06-03T023045.696.xlsx', barcode_csv_file, 1, 0)
generate_barcodes_template('./detail0909.xls', '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-09-01T235115.196.xlsx', barcode_csv_file, 1, 0)

#generate_barcodes_template('./detail2108.xls', '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-08-19T131924.801.xlsx', barcode_csv_file, 1, 0)


#Для беру
#generate_barcodes_template('/home/stani/Загрузки/детализация заказа ИП Алиев ТР (50_1).xls', '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-06-16T001553.051.xlsx', barcode_csv_file, 1, 2)

#templates
#generate_barcodes_template('detail_70_140_pack.xls', '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-08-19T131924.801.xlsx', barcode_csv_file, 100, 0)
#
# boxes = parse("/home/stani/ЗагрузкиПолотенце 40 х70 белое (itu)/МИКС_от_feb_22.xlsx")s
# full_check(boxes)s
# print('all checks is OK')
# groupped = prepare_boxes_for_deficit(boxes, [1235])
# writeDefBoxesToExcel(groupped)




repeat_rows('Описание для этикетки 2.csv', 'out.csv')

