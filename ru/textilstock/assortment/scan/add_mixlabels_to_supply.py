import pandas as pd

import os

current_path = os.path.dirname(os.path.abspath(__file__)) + '/'


def remove_ouput_files(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def add_box_barcodes(boxes_file, barcodes_file):
    remove_ouput_files('output_barcodes')
    labeled_boxes = pd.read_csv(current_path + boxes_file)
    barcodes = pd.read_excel(barcodes_file, header=None)
    barcodes['ШК короба'] = barcodes.get(0)
    barcodes['rn'] = barcodes.index + 1
    labeled_boxes.to_csv('aa.csv')
    boxes_with_barcodes = pd.merge(labeled_boxes, barcodes,
                                   how='left', left_on=['номер короба'],
                                   right_on=['rn']
                                   )
    no_box = boxes_with_barcodes[boxes_with_barcodes['номер короба'].isnull()]
    no_rn = boxes_with_barcodes[boxes_with_barcodes['rn'].isnull()]
    if len(no_box) + len(no_rn) > 0:
        raise Exception('Count of boxes and barcodes must be equal')
    boxes_with_barcodes = boxes_with_barcodes.rename(columns={"Баркод": "ШК единицы товара",
                                                              "количество": "Кол-во товаров"})
    boxes_with_barcodes = pd.DataFrame(data=boxes_with_barcodes,
                                       columns=['ШК единицы товара', 'Кол-во товаров', 'ШК короба',
                                                'срок годности'])
    boxes_with_barcodes.to_excel(current_path + 'output_barcodes/box_barcodes.xlsx', index=False)
    barcodes = pd.DataFrame(data=barcodes, columns=['rn', 'ШК короба'])
    barcodes.to_excel(current_path + 'output_barcodes/mapping.xlsx', index=False, header=False)


add_box_barcodes('output/1.csv', '/home/stani/Загрузки/barcodes (12).xlsx')

