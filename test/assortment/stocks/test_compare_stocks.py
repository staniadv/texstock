import filecmp
import os
import unittest

from ru.textilstock.assortment.stocks.compare_stocks import compare_stocks

current_path = os.path.dirname(os.path.abspath(__file__)) + '/'


class CheckSupplyCountsTest(unittest.TestCase):

    def test_check_supply_count(self):
        try:
            os.remove(current_path + 'out1.csv')
        except OSError:
            pass

        compare_stocks(current_path + 'djama_stocks.xls',
                       current_path + 'wildberrries_stocks.xlsx',
                       current_path + 'out1.csv')

        self.assertTrue(filecmp.cmp(current_path + 'out1.csv', current_path + 'expected1.csv'))


if __name__ == '__main__':
    unittest.main()
