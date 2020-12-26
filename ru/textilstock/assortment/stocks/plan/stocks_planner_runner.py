import os

from ru.textilstock.assortment.stocks.plan.stocks_planner import remove_ouput_files, generate_orders

djama_stocks_file = 'остатки Байрамали (68).xls'
article_plans = ['article_plan.xlsx', 'article_plan_1.xlsx']

current_path = os.path.dirname(os.path.abspath(__file__)) + '/'

remove_ouput_files(current_path + '/output')

for plan in article_plans:
    generate_orders(current_path + '/input/' + plan,
                    current_path + '/input/' + djama_stocks_file, 'order_' + plan)
    print("-------------------")
