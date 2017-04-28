from unittest import TestCase
from readability_score.calculators.fleschkincaid import *

class LibTestCase(TestCase):
    def test_bad_locale(self):
        with self.assertRaises(LookupError):
            fk = FleschKincaid("some text","bad_locale")
