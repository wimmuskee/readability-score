# -*- coding: utf-8 -*-
"""
This is the Automated Readability Index readability calculator

This tool can calculate the readability score of a text
using the Automated Readability Index.
http://en.wikipedia.org/wiki/Automated_Readability_Index

Wim Muskee, 2012-2017
wimmuskee@gmail.com

License: GPL-2
"""
from __future__ import division
from readability_score.common import getMinimumAgeFromUsGrade
from readability_score.textanalyzer import TextAnalyzer


class ARI(TextAnalyzer):
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
        if self.scores['word_count'] != 0 and self.scores['sent_count'] != 0:
            self.us_grade = (4.71 * (self.scores['letter_count']/self.scores['word_count'])) + (0.5 * (self.scores['word_count']/self.scores['sent_count'])) - 21.43
 
