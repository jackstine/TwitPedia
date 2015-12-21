class HTMLTable:
    SINGLE_PAGE = 1
    def __init__(self, numOfRows,search = None, currentPage = SINGLE_PAGE, *args):
        self.columns = []
        self.search = search
        self.numOfRows = numOfRows
        self.currentPage = int(currentPage)
        self.maxPage = int(currentPage)
        for col in args:
            self.add(col)

    def add(self, column):
        self._setMaxPage(column)
        self.columns.append(column)

    def setSearch(self, search):
        self.search = search

    def _setMaxPage(self, column):
        self.maxPage = max(self.maxPage, column.getPages())

    def headers(self):
        return [c.title for c in self.columns]

    def rows(self):
        rows = []
        for i in range(0,self.numOfRows):
            cols = []
            for c in self.columns:
                cols.append(c[i])
            rows.append(cols)
        return rows

    def hasPrevious(self):
        return self.currentPage != self.SINGLE_PAGE

    def hasNext(self):
        return self.currentPage < self.maxPage

    def previousPage(self):
        if (self.hasPrevious()):
            return self.currentPage - self.SINGLE_PAGE
        else:
            return None

    def nextPage(self):
        if (self.hasNext()):
            return self.currentPage + self.SINGLE_PAGE
        else:
            return self.maxPage

    def __iter__(self):
        for c in self.columns:
            yield c

class HTMLList:
    def __init__(self, title, rows, pages = 0):
        self.title = title
        self.htmlRows = rows
        self.pages = pages

    def __getitem__(self,key):
        try:
            return self.htmlRows[key]
        except:
            return None #BLAH

    def getPages(self):
        return self.pages

    def __len__(self):
        return len(self.htmlRows)

    def __str__(self):
        return str(self.htmlRows)
