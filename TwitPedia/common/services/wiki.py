import wikipedia

def wikiSearch(search, number = 100):
    return wikipedia.search(search, number)

if (__name__ == "__main__"):
    print wikiSearch("hello")
