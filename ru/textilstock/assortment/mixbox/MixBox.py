class MixBox:
    supplier_name = None
    brand = None
    consignee = None
    cargo_number = None
    box_num = None
    box_count = None
    sum_items_count = None
    items = None

    def __init__(self, supplier_name, brand, consignee, cargo_number, box_num, box_count, items, sum_items_count):
        self.supplier_name = supplier_name
        self.brand = brand
        self.consignee = consignee
        self.cargo_number = cargo_number
        self.box_num = box_num
        self.box_count = box_count
        self.sum_items_count = sum_items_count
        self.items = items

    def __str__(self):
        return 'MixBox(supplier_name=' + str(self.supplier_name) + \
               ', brand=' + str(self.brand) + \
               ', consignee=' + str(self.consignee) + \
               ', cargo_number=' + str(self.cargo_number) + \
               ', box_num=' + str(self.box_num) + \
               ', box_count=' + str(self.box_count) + \
               ', sum_items_count=' + str(self.sum_items_count) + \
               ', items=' + str(self.items) + \
               ')'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        """Overrides the default implementation"""
        #return self.cargo_number == other.cargo_number
        return self.__dict__ == other.__dict__

class MixBoxItem:
    def __init__(self, order_num, article, item_category, unit, count):
        self.order_num = order_num
        self.article = article
        self.item_category = item_category
        self.unit = unit
        self.count = count

    def __str__(self):
        return 'MixBoxItem(order_num=' + str(self.order_num) + \
               ', article=' + str(self.article) + \
               ', cargo_number=' + str(self.item_category) + \
               ', unit=' + str(self.unit) + \
               ', count=' + str(self.count) + ')'

    def __repr__(self):
        return self.__str__()


    def __eq__(self, other):
        """Overrides the default implementation"""
        #return self.cargo_number == other.cargo_number
        return self.__dict__ == other.__dict__
