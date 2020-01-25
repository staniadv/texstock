def check_required_fields_filled(mixBox):
    assert mixBox.supplier_name is not None
    assert mixBox.brand is not None
    assert mixBox.consignee is not None
    assert mixBox.cargo_number is not None
    assert mixBox.box_num is not None
    assert mixBox.box_count is not None
    assert mixBox.sum_items_count is not None
    assert mixBox.items is not None
    assert len(mixBox.items) > 0


def check_required_item_fields_filled(mixBoxItem):
    assert mixBoxItem.order_num is not None
    assert mixBoxItem.article is not None
    assert mixBoxItem.item_category is not None
    assert mixBoxItem.unit is not None
    assert mixBoxItem.count is not None


def check_item_sum_count_with_box_sum_count(mixBox):
    sum_item_count = sum(item.count for item in mixBox.items)
    assert sum_item_count == mixBox.sum_items_count


def check_box_sequence_in_cargo(mixBoxes):
    mix_box_cargo_dict = {}
    for mb in mixBoxes :
        cargo_num = mb.cargo_number
        if cargo_num not in mix_box_cargo_dict:
            mix_box_cargo_dict[cargo_num] = []
        mix_box_cargo_dict[cargo_num].append(mb)

    for cargo_num, mix_boxes in mix_box_cargo_dict.items():
        s = set(box.box_count for box in mix_boxes)

        #не на всех коробках одинаковое "номер короба из"
        assert len(s) == 1
        box_count = list(s)[0]
        box_nums = sorted(box.box_num for box in mix_boxes)

        #нет всех коробов в поставке
        assert list(range(1, box_count+1)) == box_nums

def full_check(mixBoxes) :
    for mixBox in mixBoxes :
        check_required_fields_filled(mixBox)
        for mixBoxItem in mixBox.items:
            check_required_item_fields_filled(mixBoxItem)
        check_item_sum_count_with_box_sum_count(mixBox)
        check_box_sequence_in_cargo(mixBoxes)





