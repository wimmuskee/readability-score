# -*- coding: utf-8 -*-
"""
This is the SMOG readability calculator

This tool can calculate the readability score of a text
using the Simple Measure Of Gobbledygook.
http://en.wikipedia.org/wiki/SMOG_%28Simple_Measure_Of_Gobbledygook%29

Wim Muskee, 2012
wimmuskee@gmail.com

License: GPL-2
"""
from __future__ import division

class SMOG:
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
        self.us_grade = (1.043 * ((self.scores['polysyllword_count'] * (30 / self.scores['sent_count']))**0.5)) + 3.1291
