# -*- coding: utf-8 -*-
"""
This is the Coleman-Liau readability calculator

This tool can calculate the readability score of a text
using the Coleman–Liau index.
http://en.wikipedia.org/wiki/Coleman-Liau_Index

Wim Muskee, 2012-2017
wimmuskee@gmail.com

License: GPL-2
"""
from readability_score.common import getMinimumAgeFromUsGrade
from readability_score.textanalyzer import TextAnalyzer


class ColemanLiau(TextAnalyzer):
    def __init__(self, text, locale='en_GB'):
        TextAnalyzer.__init__(self,text,locale)
        self.setTextScores()
        self.us_grade = 0
        self.setGrade()
        self.min_age = getMinimumAgeFromUsGrade(self.us_grade)

    def setGrade(self):
        """
        Calculates US grade as a float from the available
        text scores.
        """
        self.us_grade = (0.0588 * self.scores['wordletter_average'] * 100) - (0.296 * self.scores['wordsent_average'] * 100) - 15.8
