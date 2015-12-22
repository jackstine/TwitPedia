from ..services import Twitter, wiki

import unittest

class TestService(unittest.TestCase):

    def setUp(self):
        pass

    def test_wikiSearch(self):
        wikis = wiki.wikiSearch("hello")
        self.assertIsNotNone(wikis)

    def test_wikiSearchNumDefault(self):
        wikis = wiki.wikiSearch("hello")
        self.assertEqual(len(wikis), 50)

    def test_wikiSearchNumCustom(self):
        wikis = wiki.wikiSearch("hello",25)
        self.assertEqual(len(wikis), 25)

    def test_twitterSearch(self):
        twit = Twitter.Twit()
        twit.setAuth()
        tweets = twit.twitterSearch("hello")
        self.assertIsNotNone(tweets)

if (__name__ == '__main__'):
    unittest.main()
