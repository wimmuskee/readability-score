from unittest import TestCase
from readability_score.common import *

class CommonTestCase(TestCase):
    def test_minimum_age_rounding(self):
        # default python3 round lets 6.5 be rounded to 6
        us_grade = 1.5
        min_age = getMinimumAgeFromUsGrade(us_grade)
        self.assertEqual(min_age,7)
