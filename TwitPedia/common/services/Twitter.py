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
    tweets = t.twitterSearch("Jacob Cukjati")
    for tweet in tweets:
#        print "AUTHOR:**** " + str(tweet.author)
        print str(dir(tweet.author))
#        print "CONTRIBUTORS:**** " + str(tweet.contributors)
#        print "COORDINATES:**** " + str(tweet.coordinates)
#        print "CREATED_AT:**** " + str(tweet.created_at)
#        print "DESTROY:**** " + str(tweet.destroy)
#        print "ENTITIES:**** " + str(tweet.entities)
#        print "FAVORITE:**** " + str(tweet.favorite)
#        print "FAVORITE_COUNT:**** " + str(tweet.favorite_count)
#        print "FAVORITED:**** " + str(tweet.favorited)
#        print "GEO:**** " + str(tweet.geo)
#        print "ID:**** " + str(tweet.id)
#        print "ID_STR:**** " + str(tweet.id_str)
#        print "IN_REPLY_TO_SCREEN_NAME:**** " + str(tweet.in_reply_to_screen_name)
#        print "IN_REPLY_TO_STATUS_ID:**** " + str(tweet.in_reply_to_status_id)
#        print "IN_REPLY_TO_STATUS_ID_STR:**** " + str(tweet.in_reply_to_status_id_str)
#        print "IN_REPLY_TO_USER_ID:**** " + str(tweet.in_reply_to_user_id)
#        print "IN_REPLY_TO_USER_ID_STR:**** " + str(tweet.in_reply_to_user_id_str)
#        print "IS_QUOTE_STATUS:**** " + str(tweet.is_quote_status)
#        print "LANG:**** " + str(tweet.lang)
#        print "METADATA:**** " + str(tweet.metadata)
#        print "PARSE:**** " + str(tweet.parse)
#        print "PARSE_LIST:**** " + str(tweet.parse_list)
#        print "PLACE:**** " + str(tweet.place)
#        print "POSSIBLY_SENSITIVE:**** " + str(tweet.possibly_sensitive)
#        print "RETWEET:**** " + str(tweet.retweet)
#        print "RETWEET_COUNT:**** " + str(tweet.retweet_count)
#        print "RETWEETED:**** " + str(tweet.retweeted)
#        print "RETWEETS:**** " + str(tweet.retweets)
#        print "SOURCE:**** " + str(tweet.source)
#        print "SOURCE_URL:**** " + str(tweet.source_url)
#        print "TEXT:**** " + tweet.text
#        print "TRUNCATED:**** " + str(tweet.truncated)
#        user = tweet.user
#        print "PROFI<LE IMAGE   "  + str(user.profile_image_url)
#        print "Profile IMAGE:*** " + str(user.profile_background_image_url_https)
#        print "Profile Url:***" + str(user.screen_name)
#        print "TIME ZONE:*** " + str(user.time_zone)
#        print "URL : ****" + str(user.url)
