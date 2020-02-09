import filecmp
import os
import unittest

from ru.textilstock.assortment.tools.barcode_template_generator import generate_barcodes_template

current_path = os.path.dirname(os.path.abspath(__file__)) + '/'

class BarcodeGenerationTest(unittest.TestCase):

    def test_barcode_generation_test(self):
        try:
            os.remove(current_path + 'out1.csv')
        except OSError:
            pass

        generate_barcodes_template(current_path + 'djama_detalization.xls',
                                   '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-01-25T180900.442.xlsx',
                                   current_path + 'out1.csv', 8)
        self.assertTrue(filecmp.cmp(current_path + 'out1.csv', current_path + 'expected1.csv'))


if __name__ == '__main__':
    unittest.main()
