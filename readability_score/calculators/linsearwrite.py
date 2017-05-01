# -*- coding: utf-8 -*-
"""
This is the LinsearWrite readability calculator

This tool can calculate the readability score of a text
using the Linsear Write readability metric.

https://en.wikipedia.org/wiki/Linsear_Write

Wim Muskee, 2017
wimmuskee@gmail.com

License: GPL-2
"""
from __future__ import division
from readability_score.common import getMinimumAgeFromUsGrade
from readability_score.textanalyzer import TextAnalyzer


class LinsearWrite(TextAnalyzer):
    def __init__(self, text, locale='en_GB'):
        TextAnalyzer.__init__(self,text,locale)
        self.setTextScores()
        self.us_grade = 0
        self.setGrade()
        self.min_age = getMinimumAgeFromUsGrade(self.us_grade)

    def setGrade(self):
        if self.scores["sent_count"] != 0:
            score = ((self.scores["polysyllword_count"] * 3) + self.scores['word_count'] - self.scores["polysyllword_count"]) / self.scores["sent_count"]

            if score > 20:
                self.us_grade = score / 2
            else:
                self.us_grade = (score - 2) / 2
