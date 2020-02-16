from ru.textilstock.assortment.mixbox.MixBoxChecker import full_check
from ru.textilstock.assortment.mixbox.MixBoxXlsParser import parse
import pandas as pd


def get_mixbox_by_cargo_num(mix_boxes, cargo_number):
    result = []
    for mix_box in mix_boxes:
        if mix_box.cargo_number == cargo_number:
            result.append(mix_box)
    return result


def prepare_boxes_for_deficit(boxes, cargo_nums):
    cargo_mixboxes_list = []
    for cargo_num in cargo_nums :
        cargo_mixboxes_list.append(get_mixbox_by_cargo_num(boxes, cargo_num))

    print(cargo_mixboxes_list)

    item_data = []
    for cargo_mixboxes in cargo_mixboxes_list:
        for mix_box in cargo_mixboxes:
            for item in mix_box.items:
                a_and_c = item.article.split('/')
                item_data.append([mix_box.brand, a_and_c[0] + '/', a_and_c[1], item.item_category, item.count]);

    df = pd.DataFrame(item_data, columns=['Brand', 'Article', 'Color', 'Category', 'Count'])
    print(df)
    df.to_excel("o1.xlsx")

    return df.groupby(["Article", "Color", "Category"])["Count"].sum()


def writeDefBoxesToExcel(df_groupped):
    df_groupped.to_excel("output.xlsx", merge_cells=False)


# boxes = parse("/home/stani/Загрузки/МИКС_feb_08.xlsx")
# full_check(boxes)
# print('all checks is OK')
# groupped = prepare_boxes_for_deficit(boxes, [1234])
# writeDefBoxesToExcel(groupped)
