class HTMLTable:
    def __init__(self, numOfRows, *args):
        self.columns = []
        self.numOfRows = numOfRows
        for col in args:
            self.add(col)

    def add(self, column):
        self.columns.append(column)

    def headers(self):
        return [c.title for c in self.columns]

    def __iter__(self):
        for c in self.columns:
            yield c

    def rows(self):
        rows = []
        for i in range(0,self.numOfRows):
            cols = []
            for c in self.columns:
                cols.append(c[i])
            rows.append(cols)
        return rows


class HTMLList:

    def __init__(self, title, rows):
        self.title = title
        self.htmlRows = rows

    def __getitem__(self,key):
        try:
            return self.htmlRows[key]
        except:
            return None #BLAH

    def __len__(self):
        return len(self.rows)
