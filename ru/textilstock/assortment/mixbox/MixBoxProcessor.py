from ru.textilstock.assortment.mixbox.MixBox import MixBox, MixBoxItem
from ru.textilstock.assortment.mixbox.MixBoxChecker import full_check
from ru.textilstock.assortment.mixbox.MixBoxXlsParser import parse
import pandas as pd


def get_mixbox_by_cargo_num(mix_boxes, cargo_number):
    result = []
    for mix_box in mix_boxes:
        if mix_box.cargo_number == cargo_number:
            result.append(mix_box)
    return result

#boxes = parse("/home/stani/Загрузки/Образец на коробку МИКС 1111_36_by_10.xlsx")
boxes = parse("/home/stani/Загрузки/МИКС_от_19jan.xlsx")
full_check(boxes)
print('all checks is OK')

cargo_mixboxes = get_mixbox_by_cargo_num(boxes, 1235)
print(cargo_mixboxes)

item_data = []
for mix_box in cargo_mixboxes:
    for item in mix_box.items:
        a_and_c = item.article.split('/')
        item_data.append([mix_box.brand, a_and_c[0]+'/', a_and_c[1], item.item_category, item.count]);

df = pd.DataFrame(item_data, columns= ['Brand', 'Article', 'Color', 'Category', 'Count'])
print(df)
df.to_excel("o1.xlsx")

df_groupped = df.groupby(["Article", "Color", "Category"])["Count"].sum()


df_groupped.to_excel("output.xlsx", merge_cells=False)

