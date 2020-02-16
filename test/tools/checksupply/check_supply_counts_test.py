import filecmp
import os
import unittest

from ru.textilstock.assortment.tools.checksupply.check_supply_counts import generate_detalizaion_supply_diff_csv

current_path = os.path.dirname(os.path.abspath(__file__)) + '/'


class CheckSupplyCountsTest(unittest.TestCase):

    def test_check_supply_count(self):
        try:
            os.remove(current_path + 'out1.csv')
        except OSError:
            pass

        generate_detalizaion_supply_diff_csv(['detailzation.xls'],
                                             'mix_supply.xlsx',
                                             [1234, 1235],
                                             'nomenclautres.xlsx',
                                             'out1.csv')
        self.assertTrue(filecmp.cmp(current_path + 'out1.csv', current_path + 'expected1.csv'))


if __name__ == '__main__':
    unittest.main()
