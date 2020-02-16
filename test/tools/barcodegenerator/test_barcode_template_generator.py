import filecmp
import os
import unittest

from ru.textilstock.assortment.tools.barcodegenerator.barcode_template_generator import generate_barcodes_template

current_path = os.path.dirname(os.path.abspath(__file__)) + '/'

class BarcodeGenerationTest(unittest.TestCase):

    def test_barcode_generation_test(self):
        try:
            os.remove(current_path + 'out1.csv')
        except OSError:
            pass

        generate_barcodes_template(current_path + 'djama_detalization.xls',
                                   current_path + 'nomen.xlsx',
                                   current_path + 'out1.csv', 8)
        self.assertTrue(filecmp.cmp(current_path + 'out1.csv', current_path + 'expected1.csv'))


if __name__ == '__main__':
    unittest.main()
