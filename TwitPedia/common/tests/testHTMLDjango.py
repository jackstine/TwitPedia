from django.test import TestCase
from ..html.services.ServiceHTML import *

class HTMLDjangoTestCase(TestCase):

    def test_createTwitPediaTable(self):
        twitPedia = createTwitPediaTable(2,"hello")
        self.assertEqual(twitPedia.headers(),["Wikipedia","Twitter"])
        self.assertEqual(twitPedia.hasPrevious(), True)
        self.assertEqual(twitPedia.hasNext(), True)
        self.assertEqual(twitPedia.previousPage(), 1)
        self.assertEqual(twitPedia.nextPage(), 3)
        self.assertIsNotNone(twitPedia.rows())
