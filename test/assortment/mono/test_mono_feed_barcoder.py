import filecmp
import os
import unittest

from ru.textilstock.assortment.mono.mono_feed_barcoder import generate_handbook_and_template

current_path = os.path.dirname(os.path.abspath(__file__)) + '/'


class CheckSupplyCountsTest(unittest.TestCase):

    def test_check_supply_count(self):
        try:
            os.remove(current_path + 'out1.csv')
        except OSError:
            pass

        generate_handbook_and_template(current_path + 'mono_feed.xlsx',
                                       current_path +'nomen.xlsx',
                                       current_path +'wildberries_barcodes_list.xlsx',
                                       current_path +'out1.csv', current_path +'output1.xlsx')
        self.assertTrue(filecmp.cmp(current_path + 'out1.csv', current_path + 'expected1.csv'))


if __name__ == '__main__':
    unittest.main()


