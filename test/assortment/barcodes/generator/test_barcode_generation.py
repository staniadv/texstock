import filecmp
import os
import unittest

from ru.textilstock.assortment.barcodes.generator.multiple_barcodes import gen_and_write_barcodes

current_path = os.path.dirname(os.path.abspath(__file__)) + '/'


class BarcodeGenerationTest(unittest.TestCase):

    def test_gen_and_write_barcodes(self):
        try:
            os.remove(current_path + 'out1.csv')
        except OSError:
            pass

        gen_and_write_barcodes(current_path + 'barcode_data.csv', current_path + 'out1.csv')
        self.assertTrue(filecmp.cmp(current_path + 'out1.csv', current_path + 'expected1.csv'))


if __name__ == '__main__':
    unittest.main()
