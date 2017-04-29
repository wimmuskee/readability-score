from unittest import TestCase, skipIf
from sys import version_info
from readability_score.calculatortest import CalculatorTest
from readability_score.calculators.fleschkincaid import *

class UnicodeTestCase(TestCase,CalculatorTest):
    def setUp(self):
        CalculatorTest.__init__(self, 23)

    @skipIf(version_info.major > 2, "specific python2 test")
    def test_unicode_stringimport(self):
        self.calc = FleschKincaid(unicode(self.text_ro, "utf-8"),'ro_RO')
        self.assertIn(self.calc.min_age, self.test_range, self.test_range_fail_text)

    def test_regular_stringimport(self):
        self.calc = FleschKincaid(self.text_ro,'ro_RO')
        self.assertIn(self.calc.min_age, self.test_range, self.test_range_fail_text)
