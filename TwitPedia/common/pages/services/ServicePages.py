from ...services.wiki import *
from ..Pager import getPages

def wikiPage(page, query, numToSearch = 100, numToPage = 10):  #TODO props create a little datastructure, to many parameters
    wikis = wikiSearch(query, numToSearch)
    return getPages(page, wikis, numToPage)


if (__name__ == "__main__"):
    print wikiPage(1, "hello")
