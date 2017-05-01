from unittest import TestCase, expectedFailure
from readability_score.calculatortest import CalculatorTest
from readability_score.calculators.linsearwrite import *

class LinsearWriteTestCase(TestCase,CalculatorTest):
    def setUp(self):
        CalculatorTest.__init__(self, 21)

    def test_range_min_age(self):
        self.calc = LinsearWrite(self.text)
        self.assertIn(self.calc.min_age, self.test_range, self.test_range_fail_text)

    @expectedFailure
    def test_exact_min_age(self):
        self.calc = LinsearWrite(self.text)
        self.assertEqual(self.calc.min_age, self.min_age_test, "might break because of deps")

    def test_not_negative_min_age(self):
        self.calc = LinsearWrite("")
        self.assertGreaterEqual(self.calc.min_age, 0, "even with no text, min_age should not be negative")
