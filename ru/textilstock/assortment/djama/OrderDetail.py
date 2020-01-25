class OrderDetail:
    def __init__(self, article, count, price):
        self.article = article
        self.count = count
        self.price = price

    def __str__(self):
        return 'OrderDetail(article=' + self.article + \
               ', price=' + str(self.price) + \
               ', count=' + str(self.count) + \
               ')'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
