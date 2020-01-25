import re
import json
import csv
import os
import requests

# with open('/home/stani/1.html', 'r') as myfile:
#   html = myfile.read()

# r = requests.get("https://www.wildberries.ru/catalog/8330093/detail.aspx?targetUrl=BP")
# source_str = r.text


def getNomenclature(source_str) :
    str = re.search("(?<=data: ){.*}", source_str).group()

    itemData = json.loads(str)

    nomenclatures = itemData['nomenclatures']
    res = dict()


    for key in nomenclatures:
        d = dict()
        res[key] = d
        d['goodsName'] = itemData['goodsName']
        d['ordersCount'] = nomenclatures[key]['ordersCount']
        d['rusName'] = nomenclatures[key]['rusName']
        sizes = nomenclatures[key]['sizes']
        for size_key in sizes:
            d['size'] = size_key
            d['priceWithSale'] = sizes[size_key]['priceWithSale']
            d['characteristicId'] = sizes[size_key]['characteristicId']

    return res


def wirteResToCsv(res) :
    def WriteDictToCSV(csv_file,csv_columns,dict_data):
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)

    csv_columns = ['nomenclature', 'goodsName', 'color', 'priceWithSale', 'ordersCount', 'size', 'characteristicId']

    currentPath = os.getcwd()
    csv_file = currentPath + "/csv/Names.csv"


    for_csv_list = list()
    for key in res:
        for_csv = dict()
        for_csv['nomenclature'] = key

        for_csv['goodsName'] = res[key]['goodsName']
        for_csv['color'] = res[key]['rusName']
        for_csv['ordersCount'] = res[key]['ordersCount']
        for_csv['size'] = res[key]['size']
        for_csv['priceWithSale'] = res[key]['priceWithSale']
        for_csv['characteristicId'] = res[key]['characteristicId']
        for_csv_list.append(for_csv)

    WriteDictToCSV(csv_file, csv_columns, for_csv_list)


with open('/home/stani/1.html', 'r') as myfile:
  src = myfile.read()

nomen = getNomenclature(src)
print(nomen)
wirteResToCsv(nomen)




