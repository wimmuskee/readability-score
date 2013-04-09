# -*- coding: utf-8 -*-
"""
This is the Flesch-Kincaid readability calculator

This tool can calculate the readability score of a text
using the Flesch-Kincaid Grade Level.
http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_test

Wim Muskee, 2012
wimmuskee@gmail.com

License: GPL-2
"""

class FleschKincaid:
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
        self.us_grade = (0.39 * self.scores['sentlen_average']) + (11.8 * self.scores['wordlen_average']) - 15.59
