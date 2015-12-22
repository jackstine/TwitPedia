from ..pages import Pager
from ..pages.services.ServicePages import *

import unittest

class TestPager(unittest.TestCase):

    def setUp(self):
        self.listOfObjs = list(range(0,100))

    def test_getPagesDefault(self):
        obj = Pager.getPages(1,self.listOfObjs)
        self.assertEquals(len(obj), 10)
        self.assertEquals(str(obj), "<Page 1 of 10>")
        for i,o in enumerate(obj):
            self.assertEquals(i,o)

    def test_getPagesCustom(self):
        obj = Pager.getPages(1,self.listOfObjs,20)
        self.assertEquals(len(obj), 20)
        self.assertEquals(str(obj), "<Page 1 of 5>")
        for i,o in enumerate(obj):
            self.assertEquals(i,o)

    def test_getPagesThirdPage(self):
        obj = Pager.getPages(3,self.listOfObjs,10)
        self.assertEquals(len(obj), 10)
        self.assertEquals(str(obj), "<Page 3 of 10>")
        for i,o in enumerate(obj):
            self.assertEquals(i + 20,o)

    def test_wikiPage(self):
        wikiObjs = wikiPage(1, "hello")
        self.assertEquals(len(wikiObjs), 10)
        
    def test_twitterSearchPage(self):
        tweets = twitterSearchPage(1,"hello")
        self.assertEquals(len(tweets), 10)
        self.assertEquals(str(tweets), "<Page 1 of 2>")
           
if (__name__ == "__main__"):
    unittest.main()
