import pandas as pd

from ru.textilstock.assortment.djama.xls.join_detail_and_nomen import join_djama_detail_with_nomen
from ru.textilstock.assortment.djama.xls.order_detalization_parser import parse_order_detalizations
from ru.textilstock.assortment.mixbox.MixBoxChecker import full_check
from ru.textilstock.assortment.mixbox.MixBoxProcessor import prepare_boxes_for_deficit
from ru.textilstock.assortment.mixbox.MixBoxXlsParser import parse


def generate_detalizaion_supply_diff_csv(detalization_files_xlsx,
                                         mix_supply_csv,
                                         mixbox_cargo_nums,
                                         nomenclature_file_xls,
                                         out_diff_file):
    boxes = parse(mix_supply_csv)
    full_check(boxes)
    groupped_boxes = prepare_boxes_for_deficit(boxes, mixbox_cargo_nums).to_frame().reset_index()

    order_details_df = parse_order_detalizations(detalization_files_xlsx)
    data = []
    for order in order_details_df:
        data.append([order.article, order.count, order.price])
    df = pd.DataFrame(data=data, columns=['article', 'count', 'price'])
    detail_with_nomen_df = join_djama_detail_with_nomen(df, nomenclature_file_xls)
    #
    # print(detail_with_nomen_df)
    # detail_with_nomen_df.to_csv('2.csv')

    df = pd.merge(groupped_boxes, detail_with_nomen_df,
                  how='outer', left_on=['Article', 'Color'],
                  right_on=['Артикул ИМТ', 'Артикул Цвета']
                  )

    df.to_csv(out_diff_file)


# generate_detalizaion_supply_diff_csv(['detail2.xls'], '/home/stani/Загрузки/МИКС_feb_15.xlsx',
#                                      [1234, 1235],
#                                      '/home/stani/Загрузки/ExportToEXCELOPENXML - 2020-01-25T180900.442.xlsx',
#                                      '3.csv')
