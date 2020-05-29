from ru.textilstock.assortment.barcodes.generator.multiple_barcodes import gen_and_write_barcodes
from ru.textilstock.assortment.djama.xls.order_detalization_parser import parse_order_detalizations
from ru.textilstock.assortment.mixbox.MixBoxChecker import full_check
from ru.textilstock.assortment.mixbox.MixBoxXlsParser import parse
from ru.textilstock.assortment.mixbox.MixBoxProcessor import prepare_boxes_for_deficit, writeDefBoxesToExcel
from ru.textilstock.assortment.tools.barcodegenerator.barcode_template_generator import generate_barcodes_template

barcode_csv_file = 'barcodes.csv'

# gen_and_write_barcodes('ExportToEXCELOPENXML - 2020-02-02T022159.922.csv', 'ituma.csv')
#
# barcode_csv_file = 'barcodes.csv'
#Полотенце 150 х210 сиреневый (itu)
# generate_barcodes_template('detail.xls',
#                            '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-04-09T184919.179.xlsx',
#                            barcode_csv_file, 8)

generate_barcodes_template('detail1.xls', 'spec.xlsx', barcode_csv_file, 1, 4)
#
# boxes = parse("/home/stani/Загрузки/МИКС_от_feb_22.xlsx")
# full_check(boxes)
# print('all checks is OK')
# groupped = prepare_boxes_for_deficit(boxes, [1235])
# writeDefBoxesToExcel(groupped)
