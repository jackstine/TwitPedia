from ..html.base import *
from ..html.services.ServiceHTML import *

import unittest

class TestHTML(unittest.TestCase):

    def setUp(self):
        self.hundred = range(0,100)
        self.ten = range(0,10)
        self.tenTitle = "ten"
        self.hundredTitle = "hundred"
        self.tenList = HTMLList(self.tenTitle,self.ten)
        self.hundredList = HTMLList(self.hundredTitle,self.hundred)
        self.numOfRows = 10
        self.theTable = HTMLTable(self.numOfRows,None,1,self.tenList, self.hundredList)

    def test_HTMList(self):
        for i in range(0,10):
            self.assertEquals(self.tenList[i],i)
        self.assertEquals(len(self.tenList),10)
        self.assertEquals(len(self.hundredList),100)
        self.assertEquals(str(self.tenList),str(self.ten))
        self.assertEquals(str(self.hundredList),str(self.hundredList))
        self.assertEquals(self.tenList.title, self.tenTitle)
        self.assertEquals(self.hundredList.title, self.hundredTitle)
        self.assertEquals(self.tenList.getPages(),0)

    def test_HTMLTable(self):
        search = "numbers"
        self.theTable.setSearch(search)
        self.assertEquals(self.theTable.search,search)
        self.assertEquals(self.theTable.headers(), [self.tenTitle, self.hundredTitle])
        for i, row in enumerate(self.theTable.rows()):
            self.assertEquals(row, [i,i])

    def test_createWikiList(self):
        wikiList = createWikiList(2,"hello")
        self.assertEquals(wikiList.title, "Wikipedia")
        self.assertIsNotNone(wikiList.getPages)
        self.assertIsNotNone(wikiList.htmlRows)

    def test_createTwitterList(self):
        twitterList = createTwitterList(2,"hello")
        self.assertEquals(twitterList.title, "Twitter")
        self.assertIsNotNone(twitterList.getPages)
        self.assertIsNotNone(twitterList.htmlRows)

if (__name__ == "__main__"):
    unittest.main()
