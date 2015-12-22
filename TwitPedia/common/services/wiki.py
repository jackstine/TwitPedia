import wikipedia

def wikiSearch(search, number = 50):
    return wikipedia.search(search, number)

if (__name__ == "__main__"):
    print wikiSearch("hello")
