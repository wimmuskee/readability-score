from unittest import TestCase
from readability_score.calculators.fleschkincaid import *

class LibTestCase(TestCase):
    def test_bad_locale(self):
        with self.assertRaises(LookupError):
            fk = FleschKincaid("some text","bad_locale")

    def test_good_locale(self):
        try:
            fk = FleschKincaid("some text","nl_NL")
        except:
            fk = None
        self.assertTrue(hasattr(fk,"scores"),"calculator not made with non default but correct locale")
