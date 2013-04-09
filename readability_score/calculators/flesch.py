# -*- coding: utf-8 -*-
"""
This is the Flesch Reading Ease readability calculator

This tool can calculate the readability score of a text
using the Flesch Reading Ease algorithm.
http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_test

This calculator won't export a grade level or minimum age, but only
the score for reading ease.

Wim Muskee, 2013
wimmuskee@gmail.com

License: GPL-2
"""

class Flesch:
    def __init__(self, text, locale='en_GB'):
        from readability_score.common import getTextScores

        self.scores = getTextScores(text, locale)
        self.reading_ease = 206.835 - ( 1.015 * self.scores['sentlen_average'] ) - ( 84.6 * self.scores['wordlen_average'] )
