import os
import unittest
from ru.textilstock.assortment.djama.xls.order_detalization_parser import parse_order_detalization
from ru.textilstock.assortment.djama.OrderDetail import OrderDetail

current_path = os.path.dirname(os.path.abspath(__file__)) + '/'

class OrderDetailTest(unittest.TestCase):

    def test_parse_orders(self):
        expected = [
            OrderDetail(article='Полотенце 150 х210 бирюзовый (itu)', count=4, price=536.0),
            OrderDetail(article='Полотенце 180 х210 белое (itu)', count=8, price=643.0),
            OrderDetail(article='Полотенце 70 х140 оранжевый (itu)', count=25, price=167.0),
        ]
        actual = parse_order_detalization(current_path + 'order_detail_sample.xls')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
