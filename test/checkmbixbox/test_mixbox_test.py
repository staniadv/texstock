import unittest

from ru.textilstock.assortment.mixbox.MixBox import MixBox, MixBoxItem
from ru.textilstock.assortment.mixbox.MixBoxChecker \
    import check_required_fields_filled, check_required_item_fields_filled, \
    check_item_sum_count_with_box_sum_count, check_box_sequence_in_cargo, full_check


class CheckMixBoxTest(unittest.TestCase):

    def test_full_check_success(self):
        mixboxes = [MixBox(supplier_name='ИП Алиев Т.Р.',
                        consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                        cargo_number=610790, box_num=1, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', 'шт', 10)]),
                    MixBox(supplier_name='ИП Алиев Т.Р.',
                           consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                           cargo_number=610790, box_num=2, box_count=2,
                           sum_items_count=12, brand='Байрамали',
                           items=[MixBoxItem(1, 'abc/223', 'Полотенца', 'шт', 12)])
                    ]
        full_check(mixboxes)


    def test_check_mix_boxes_success(self):
        mixbox = MixBox(supplier_name='ИП Алиев Т.Р.',
                        consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                        cargo_number=610790, box_num=1, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', 'шт', 10)])
        check_required_fields_filled(mixbox)
        for item in mixbox.items:
            check_required_item_fields_filled(item)

    def test_check_mix_boxes_none_supplier(self):
        mixbox = MixBox(supplier_name=None,
                        consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                        cargo_number=610790, box_num=1, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', 'шт', 10)])

        with self.assertRaises(AssertionError):
            check_required_fields_filled(mixbox)

    def test_check_mix_boxes_none_consignee(self):
        mixbox = MixBox(supplier_name='Ололо',
                        consignee=None,
                        cargo_number=610790, box_num=1, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', 'шт', 10)])

        with self.assertRaises(AssertionError):
            check_required_fields_filled(mixbox)

    def test_check_mix_boxes_none_cargo_num(self):
        mixbox = MixBox(supplier_name='Ололо',
                        consignee='abc',
                        cargo_number=None, box_num=1, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', 'шт', 10)])

        with self.assertRaises(AssertionError):
            check_required_fields_filled(mixbox)

    def test_check_mix_boxes_none_box_num(self):
        mixbox = MixBox(supplier_name='Ололо',
                        consignee='abc',
                        cargo_number=123, box_num=None, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', 'шт', 10)])

        with self.assertRaises(AssertionError):
            check_required_fields_filled(mixbox)

    def test_check_mix_boxes_none_box_count(self):
        mixbox = MixBox(supplier_name='Ололо',
                        consignee='abc',
                        cargo_number=123, box_num=1, box_count=None,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', 'шт', 10)])
        with self.assertRaises(AssertionError):
            check_required_fields_filled(mixbox)

    def test_check_mix_boxes_none_sum_items_count(self):
        mixbox = MixBox(supplier_name='Ололо',
                        consignee='abc',
                        cargo_number=123, box_num=1, box_count=10,
                        sum_items_count=None, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', 'шт', 10)])
        with self.assertRaises(AssertionError):
            check_required_fields_filled(mixbox)

    def test_check_mix_boxes_none_sum_brand(self):
        mixbox = MixBox(supplier_name='Ололо',
                        consignee='abc',
                        cargo_number=123, box_num=1, box_count=10,
                        sum_items_count=12, brand=None,
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', 'шт', 10)])
        with self.assertRaises(AssertionError):
            check_required_fields_filled(mixbox)

    def test_check_mix_boxes_none_items(self):
        mixbox = MixBox(supplier_name='Ололо',
                        consignee='abc',
                        cargo_number=123, box_num=1, box_count=10,
                        sum_items_count=12, brand='abc',
                        items=None)
        with self.assertRaises(AssertionError):
            check_required_fields_filled(mixbox)

        def test_check_mix_boxes_none_items(self):
            mixbox = MixBox(supplier_name='Ололо',
                            consignee='abc',
                            cargo_number=123, box_num=1, box_count=10,
                            sum_items_count=12, brand='abc',
                            items=[])
            with self.assertRaises(AssertionError):
                check_required_fields_filled(mixbox)

    def test_check_mix_boxes_item_order_num(self):
        mixbox = MixBox(supplier_name='ИП Алиев Т.Р.',
                        consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                        cargo_number=610790, box_num=1, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(None, 'abc/123', 'Полотенца', 'шт', 10)])
        check_required_fields_filled(mixbox)
        with self.assertRaises(AssertionError):
            for item in mixbox.items:
                check_required_item_fields_filled(item)

    def test_check_mix_boxes_item_article(self):
        mixbox = MixBox(supplier_name='ИП Алиев Т.Р.',
                        consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                        cargo_number=610790, box_num=1, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, None, 'Полотенца', 'шт', 10)])
        check_required_fields_filled(mixbox)
        with self.assertRaises(AssertionError):
            for item in mixbox.items:
                check_required_item_fields_filled(item)

    def test_check_mix_boxes_item_category(self):
        mixbox = MixBox(supplier_name='ИП Алиев Т.Р.',
                        consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                        cargo_number=610790, box_num=1, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', None, 'шт', 10)])
        check_required_fields_filled(mixbox)
        with self.assertRaises(AssertionError):
            for item in mixbox.items:
                check_required_item_fields_filled(item)

    def test_check_mix_boxes_item_unit(self):
        mixbox = MixBox(supplier_name='ИП Алиев Т.Р.',
                        consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                        cargo_number=610790, box_num=1, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', None, 10)])
        check_required_fields_filled(mixbox)
        with self.assertRaises(AssertionError):
            for item in mixbox.items:
                check_required_item_fields_filled(item)

    def test_check_mix_boxes_item_count(self):
        mixbox = MixBox(supplier_name='ИП Алиев Т.Р.',
                        consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                        cargo_number=610790, box_num=1, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', 'шт', None)])
        check_required_fields_filled(mixbox)
        with self.assertRaises(AssertionError):
            for item in mixbox.items:
                check_required_item_fields_filled(item)

    def test_check_items_sum_count_with_box_sum_count_success(self):
        mixbox = MixBox(supplier_name='ИП Алиев Т.Р.',
                        consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                        cargo_number=610790, box_num=1, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', 'шт', 9),
                               MixBoxItem(1, 'abc/125', 'Полотенца', 'шт', 1)])
        check_item_sum_count_with_box_sum_count(mixbox)

    def test_check_items_sum_count_with_box_sum_count_missmatch(self):
        mixbox = MixBox(supplier_name='ИП Алиев Т.Р.',
                        consignee='г.МОСКВА ООО "ВАЙЛДБЕРРИЗ"',
                        cargo_number=610790, box_num=1, box_count=2,
                        sum_items_count=10, brand='Байрамали',
                        items=[MixBoxItem(1, 'abc/123', 'Полотенца', 'шт', 9),
                               MixBoxItem(1, 'abc/125', 'Полотенца', 'шт', 2)])
        with self.assertRaises(AssertionError):
            check_item_sum_count_with_box_sum_count(mixbox)

    def test_check_box_sequense_in_cargo(self):
        boxes = [
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=1, box_count=4,sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=2, box_count=4,sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=3, box_count=4,sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=4, box_count=4,sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None, cargo_number=610791,
                   box_num=1, box_count=2, sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None, cargo_number=610791,
                   box_num=2, box_count=2, sum_items_count=None, brand=None, items=[]),
        ]
        check_box_sequence_in_cargo(boxes)

    def test_check_diffrent_box_count(self):
        boxes = [
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=1, box_count=3,sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=2, box_count=3,sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=3, box_count=2,sum_items_count=None, brand=None, items=[])
        ]
        with self.assertRaises(AssertionError):
            check_box_sequence_in_cargo(boxes)

    def test_check_illegal_box_nums(self):
        boxes = [
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=1, box_count=3,sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=2, box_count=3,sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=2, box_count=3,sum_items_count=None, brand=None, items=[])
        ]
        with self.assertRaises(AssertionError):
            check_box_sequence_in_cargo(boxes)

    def test_check_illegal_box_num_overflow(self):
        boxes = [
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=1, box_count=3,sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=2, box_count=3,sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=4, box_count=3,sum_items_count=None, brand=None, items=[])
        ]
        with self.assertRaises(AssertionError):
            check_box_sequence_in_cargo(boxes)



    def test_check_row_num_order_not_important(self):
        boxes = [
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=1, box_count=3,sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=3, box_count=3,sum_items_count=None, brand=None, items=[]),
            MixBox(supplier_name=None, consignee=None,cargo_number=610790,
                   box_num=2, box_count=3,sum_items_count=None, brand=None, items=[])
        ]


if __name__ == '__main__':
    unittest.main()
