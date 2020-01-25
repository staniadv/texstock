import re
import json
import csv
import os
import requests

# with open('/home/stani/2.html', 'r') as myfile:
#   html = myfile.read()

# r = requests.get("https://www.wildberries.ru/catalog/8330093/detail.aspx?targetUrl=BP")
# source_str = r.text


def getCart(source_str) :
    str = re.search("(?<=data: ){.*}", source_str).group()

    itemData = json.loads(str)

    items = itemData['basketItems']

    res = list()

    for item in items:
        res_item = dict()
        res_item['cod1S'] = item['cod1S']
        res_item['goodsName'] = item['goodsName']
        res_item['colorName'] = item['colorName']
        res_item['priceWithSale'] = item['priceWithSale']
        res_item['priceWithCoupon']= item['priceWithCoupon']
        res_item['maxQuantity']= item['maxQuantity']
        res.append(res_item)

    return res




    # res = dict()
    #
    #
    # for key in nomenclatures:
    #     d = dict()
    #     res[key] = d
    #     d['goodsName'] = itemData['goodsName']
    #     d['ordersCount'] = nomenclatures[key]['ordersCount']
    #     d['rusName'] = nomenclatures[key]['rusName']
    #     sizes = nomenclatures[key]['sizes']
    #     for size_key in sizes:
    #         d['size'] = size_key
    #         d['priceWithSale'] = sizes[size_key]['priceWithSale']
    #         d['characteristicId'] = sizes[size_key]['characteristicId']
    #
    # return res


def wirteResToCsv(res) :
    def WriteDictToCSV(csv_file,csv_columns,dict_data):
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)

    csv_columns = ['cod1S', 'goodsName', 'colorName', 'priceWithSale', 'priceWithCoupon', 'maxQuantity']

    currentPath = os.getcwd()
    csv_file = currentPath + "/csv/cart.csv"

    print(res)
    WriteDictToCSV(csv_file, csv_columns, res)


with open('/home/stani/wildberries/cart.html', 'r') as myfile:
  src = myfile.read()

cart = getCart(src)
print(cart)
wirteResToCsv(cart)




