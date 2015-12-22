from ...pages.services.ServicePages import wikiPage, twitterSearchPage
from ...html.base import HTMLList, HTMLTable
from django.template.loader import render_to_string

def createWikiList(page, query, numToSearch = 50, numToPage = 10):
    try:
        wikiPages = wikiPage(page, query, numToSearch, numToPage)
        htmlRows = [render_to_string('shared/wiki.html', { 'wiki':sec}) for sec in wikiPages]
        return HTMLList("Wikipedia", htmlRows, wikiPages.paginator.num_pages)
    except:
        return HTMLList("Wikipedia",list(),0)

def createTwitterList(page, search, numToPage = 10, geocode = None):
    try:
        twitterPages = twitterSearchPage(page, search, numToPage, geocode)
        htmlRows = [render_to_string('shared/tweet.html', { 'tweet':sec}) for sec in twitterPages]
        return HTMLList("Twitter", htmlRows, twitterPages.paginator.num_pages)
    except Exception as e:
        print e
        return HTMLList("Twitter",list(),0)

def createTwitPediaTable(page, search, numToSearch = 50,numToPage = 10,geocode = None): #TODO encapsulate in common DS
    wikiList = createWikiList(page, search, numToSearch, numToPage)
    twitterList = createTwitterList(page, search, numToPage, geocode)
    table = HTMLTable(numToPage,search, page)
    table.add(wikiList)
    table.add(twitterList) 
    return table


if (__name__ == "__main__"):
    table = createTwitPediaTable(1,1,"Warren Buffet")
    for r in table.rows():
        print r
