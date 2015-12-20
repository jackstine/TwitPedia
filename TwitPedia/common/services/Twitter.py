import tweepy

CONSUMER_KEY = "UI8UvbOJuh8WLPIjg5GaCreGX"
CONSUMER_SECRET = "8NqeQmP95jRaIHywXc2kq5DuwvyjBWeNF56MlCkwcugfFE8trg"
ACCESS_TOKEN = "459845463-u0BLmbwRs7MMXgjWKJ0ABXzhWWNI9tljmexjXImD"
ACCESS_TOKEN_SECRET = "w0o2J4EexOwn6yqThKz7GMA8cYPI8UbuauqnhXx4qKunt"

class Twit:
    auth = None
    api = None

    def __init__(self):
        self.setAuth()

    def setAuth(self):
        if(self.auth == None or self.api == None):
            self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
            self.api = tweepy.API(self.auth)

    def twitterSearch(self, search):
        self.setAuth()
        return self.api.search(search)

if (__name__ == "__main__"):
    t = Twit()
    print t.twitterSearch("warren")
