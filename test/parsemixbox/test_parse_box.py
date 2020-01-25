import os
import unittest

from ru.textilstock.assortment.mixbox.MixBoxXlsParser import parse

from ru.textilstock.assortment.mixbox.MixBox import MixBox
from ru.textilstock.assortment.mixbox.MixBox import MixBoxItem

current_path = os.path.dirname(os.path.abspath(__file__)) + '/'

class ParsePoxTest(unittest.TestCase):

    def test_two_boxes_success(self):
        actual = parse(current_path + 'two_boxes_success.xlsx')
        expected = [
            MixBox(supplier_name='ИП Алиев Т.Р.', consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                   cargo_number=610790, box_num=1, box_count=2, sum_items_count=10, brand='Байрамали',
                   items=[
                       MixBoxItem(order_num=1, article='4833001530087/светло-кремовый',
                                  item_category='Простыни', unit='шт.', count=9),
                       MixBoxItem(order_num=2, article='4833001530070/синий',
                                  item_category='Полотенца', unit='шт.', count=1)
                   ]),
            MixBox(supplier_name='ИП Алиев Т.Р.', consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                   cargo_number=610790, box_num=2, box_count=2, sum_items_count=11, brand='Байрамали',
                   items=[
                       MixBoxItem(order_num=1, article='4833001530087/зеленый',
                                  item_category='Простыни', unit='шт.', count=5),
                       MixBoxItem(order_num=2, article='4833001530063/красный',
                                  item_category='Полотенца', unit='шт.', count=6)
                   ])
        ]

        self.assertEqual(expected, actual)

    def test_cargo_empty_cargo_num_box(self):
        actual = parse(current_path + 'skip_empty_cargo_num_box.xlsx')
        expected = [
            MixBox(supplier_name='ИП Алиев Т.Р.', consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                   cargo_number=610790, box_num=2, box_count=2, sum_items_count=11, brand='Байрамали',
                   items=[
                       MixBoxItem(order_num=1, article='4833001530087/зеленый',
                                  item_category='Простыни', unit='шт.', count=5),
                       MixBoxItem(order_num=2, article='4833001530063/красный',
                                  item_category='Полотенца', unit='шт.', count=6)
                   ])
        ]

        self.assertEqual(expected, actual)

    def test_empty_box_item(self):
        actual = parse(current_path + 'empty_box_item.xlsx')
        expected = [
            MixBox(supplier_name='ИП Алиев Т.Р.', consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                   cargo_number=610790, box_num=1, box_count=1, sum_items_count=1, brand='Байрамали',
                   items=[
                       MixBoxItem(order_num=None, article=None,
                                  item_category=None, unit=None, count=None),
                       MixBoxItem(order_num=2, article='4833001530070/синий',
                                  item_category='Полотенца', unit='шт.', count=1)
                   ])
        ]

        self.assertEqual(expected, actual)

    def test_partial_empty_box_item(self):
        actual = parse(current_path + 'partial_empty_box_item.xlsx')

        expected = [
            MixBox(supplier_name='ИП Алиев Т.Р.', consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                   cargo_number=610790, box_num=1, box_count=1, sum_items_count=8, brand='Байрамали',
                   items=[
                       MixBoxItem(order_num=None, article='4833001530070/зеленый',
                                  item_category='Полотенца', unit='шт.', count=2),
                       MixBoxItem(order_num=2, article=None,
                                  item_category='Полотенца', unit='шт.', count=2),
                       MixBoxItem(order_num=3, article='4833001530070/зеленый',
                                  item_category=None, unit='шт.', count=2),
                       MixBoxItem(order_num=4, article='4833001530070/зеленый',
                                  item_category='Полотенца', unit=None, count=2),
                       MixBoxItem(order_num=5, article='4833001530070/зеленый',
                                  item_category='Полотенца', unit='шт.', count=None)
                   ])
        ]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
