# -*- coding: utf-8 -*-
"""
This is the Automated Readability Index readability calculator

This tool can calculate the readability score of a text
using the Automated Readability Index.
http://en.wikipedia.org/wiki/Automated_Readability_Index

Wim Muskee, 2012
wimmuskee@gmail.com

License: GPL-2
"""
from __future__ import division

class ARI:
    def __init__(self, text, locale='en_GB'):
        from readability_score.common import getTextScores, getMinimumAgeFromUsGrade
        
        self.us_grade = 0
        self.min_age = 0
        self.scores = getTextScores(text, locale)
        self.setGrade()
        self.min_age = getMinimumAgeFromUsGrade(self.us_grade)

    def setGrade(self):
        """
        Calculates US grade as a float from the available
        text scores.
        """
        self.us_grade = (4.71 * (self.scores['letter_count']/self.scores['word_count'])) + (0.5 * (self.scores['word_count']/self.scores['sent_count'])) - 21.43
 