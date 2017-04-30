from unittest import TestCase
from readability_score.textanalyzer import TextAnalyzer

class LibTestCase(TestCase):
    def test_bad_locale(self):
        with self.assertRaises(LookupError):
            t = TextAnalyzer("some text","bad_locale")

    def test_good_locale(self):
        try:
            t = TextAnalyzer("some text","nl_NL")
        except:
            fk = None
        self.assertTrue(hasattr(t,"scores"),"text analyzer not made with non default but correct locale")
