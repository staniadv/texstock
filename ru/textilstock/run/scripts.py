from ru.textilstock.assortment.barcodes.generator.multiple_barcodes import gen_and_write_barcodes
from ru.textilstock.assortment.tools.barcode_template_generator import generate_barcodes_template

gen_and_write_barcodes('ExportToEXCELOPENXML - 2020-02-02T022159.922.csv', 'ituma.csv')

barcode_csv_file = 'barcodes.csv'

generate_barcodes_template('1.xls',
             '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-01-25T180900.442.xlsx',
                           barcode_csv_file, 8)
