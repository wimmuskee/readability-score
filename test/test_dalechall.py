from unittest import TestCase, expectedFailure
from readability_score.calculatortest import CalculatorTest
from readability_score.calculators.dalechall import *

class DaleChallTestCase(TestCase,CalculatorTest):
    def setUp(self):
        CalculatorTest.__init__(self, 21)
        simplewords = ["is","the","a","can","text","in","of","on","its","and","such","as","line","size","ease","with","content","font","length","height"]
        self.calc = DaleChall(self.text,simplewordlist=simplewords)

    def test_range_min_age(self):
        self.assertIn(self.calc.min_age, self.test_range, self.test_range_fail_text)

    @expectedFailure
    def test_exact_min_age(self):
        self.assertEqual(self.calc.min_age, self.min_age_test, "might break because of deps")
