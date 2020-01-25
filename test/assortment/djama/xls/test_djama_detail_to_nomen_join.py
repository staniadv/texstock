import filecmp
import os
import unittest
from ru.textilstock.assortment.djama.xls.join_detail_and_nomen import join_detail_with_nomen_and_write

current_path = os.path.dirname(os.path.abspath(__file__)) + '/'

class JoinDetailWithNomen(unittest.TestCase):

    def test_parse_orders(self):
        try:
            os.remove('out1.csv')
        except OSError:
            pass
        join_detail_with_nomen_and_write(current_path + 'details.csv',current_path + 'nomen.xlsx', current_path + 'out1.csv')
        self.assertTrue(filecmp.cmp(current_path + 'out1.csv', current_path + 'expected1.csv'))


if __name__ == '__main__':
    unittest.main()
