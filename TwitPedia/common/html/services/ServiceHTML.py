from ...pages.services.ServicePages import wikiPage, twitterSearchPage
from ...html.base import HTMLList, HTMLTable
from django.template.loader import render_to_string

def createWikiList(page, query, numToSearch = 100, numToPage = 10):
    wikiPages = wikiPage(page, query, numToSearch, numToPage)
    htmlRows = [render_to_string('shared/wiki.html', { 'wiki':sec}) for sec in wikiPages]
    return HTMLList("Wikipedia", htmlRows)

def createTwitterList(page, search, numToPage = 10):
    twitterPages = twitterSearchPage(page, search, numToPage)
    htmlRows = [render_to_string('shared/tweet.html', { 'tweet':sec}) for sec in twitterPages]
    return HTMLList("Twitter", htmlRows)

def createTwitPediaTable(twitterPage, wikiPage, search, numToSearch = 100,numToPage = 10): #TODO encapsulate in common DS
    wikiList = createWikiList(wikiPage, search, numToSearch, numToPage)
    twitterList = createTwitterList(twitterPage, search, numToPage)
    table = HTMLTable(numToPage)
    table.add(wikiList)
    table.add(twitterList) 
    return table


if (__name__ == "__main__"):
    table = createTwitPediaTable(1,1,"Warren Buffet")
    for r in table.rows():
        print r
