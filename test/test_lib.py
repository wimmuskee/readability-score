from unittest import TestCase
from readability_score.textanalyzer import TextAnalyzer

class LibTestCase(TestCase):
    def test_incorrect_locale(self):
        with self.assertRaises(LookupError):
            t = TextAnalyzer("some text","bad_locale")

    def test_short_locale(self):
        with self.assertRaises(LookupError):
            t = TextAnalyzer("some text","e")

    def test_correct_locale(self):
        try:
            t = TextAnalyzer("some text","nl_NL")
        except:
            fk = None
        self.assertTrue(hasattr(t,"scores"),"text analyzer not made with non default but correct locale")

    def test_bad_simpleword_list(self):
        t = TextAnalyzer("some text")
        with self.assertRaises(ValueError):
            t.setSimpleWordsList("this string")

    def test_tokenize_language_default(self):
        t = TextAnalyzer("some text")
        self.assertEqual(t.tokenize_language,"english","default tokenize_language should be english")

    def test_tokenize_language_custom(self):
        t = TextAnalyzer("some text","nl_NL")
        self.assertEqual(t.tokenize_language,"dutch","set tokenize_language should be dutch")

    def test_tokenize_language_exotic(self):
        t = TextAnalyzer("some text","zu_ZA")
        self.assertEqual(t.tokenize_language,"english","default tokenize_language should be english")
