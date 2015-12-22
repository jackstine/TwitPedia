from ...services.wiki import *
from ...services.Twitter import *
from ..Pager import getPages

_twit = None

def wikiPage(page, query, numToSearch = 50, numToPage = 10):
    wikis = wikiSearch(query, numToSearch)
    return getPages(page, wikis, numToPage)

def twitterSearchPage(page, search, numToPage = 10):
    global _twit
    setTwitter()
    tweets = _twit.twitterSearch(search)
    return getPages(page, tweets, numToPage)


def setTwitter():
    global _twit
    if (_twit == None):
        _twit = Twit()


if (__name__ == "__main__"):
    print twitterSearchPage(1, "Warren")
