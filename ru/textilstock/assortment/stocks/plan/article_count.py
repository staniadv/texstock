class ArticleCount:
    def __init__(self, article, count):
        self.article = article
        self.count = count

    def __str__(self):
        return 'ArticleCount(article=' + self.article + \
               ', count=' + str(self.count) + \
               ')'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
