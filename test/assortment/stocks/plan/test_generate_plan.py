import filecmp
import os
import unittest

import pandas as pd

from ru.textilstock.assortment.stocks.compare_stocks import compare_stocks
from ru.textilstock.assortment.stocks.plan.stocks_planner import generate_orders

current_path = os.path.dirname(os.path.abspath(__file__)) + '/'


class CheckGenerateStocksPlanTest(unittest.TestCase):

    def test_check_generate_stocks(self):
        try:
            os.remove(current_path + 'output/order_article_plan.xlsx')
        except OSError:
            pass

        djama_stocks_file = 'djama_stocks.xls'
        article_plans = ['article_plan.xlsx']

        for plan in article_plans:
            generate_orders(current_path + '/input/' + plan,
                            current_path + '/input/' + djama_stocks_file,
                            current_path + '/output/' + 'order_' + plan)
            print("-------------------")

        expected = pd.read_excel(current_path + 'expected.xlsx')
        actual = pd.read_excel(current_path + '/output/order_article_plan.xlsx')

        self.assertTrue(actual.equals(expected))


if __name__ == '__main__':
    unittest.main()
