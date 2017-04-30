# -*- coding: utf-8 -*-
"""
This is the Dale-Chall readability calculator

This tool can calculate the readability score of a text
using the Dale-Chall Readability Formula.
http://en.wikipedia.org/wiki/Dale-Chall_Readability_Formula

This algorithm requires a lower case simple word list. 
According to the documentation, some 3000 words which are
considered easily readable.

Wim Muskee, 2012-2017
wimmuskee@gmail.com

License: GPL-2
"""
from __future__ import division
from readability_score.common import getMinimumAgeFromUsGrade
from readability_score.textanalyzer import TextAnalyzer


class DaleChall(TextAnalyzer):
    def __init__(self, text, locale='en_GB', simplewordlist=[]):
        TextAnalyzer.__init__(self,text,locale)
        self.setSimpleWordsList(simplewordlist)
        self.setTextScores()
        self.readingindex = 0
        self.us_grade = 0
        self.setReadingIndex()
        self.setGrade()
        self.min_age = getMinimumAgeFromUsGrade(self.us_grade)

    def setReadingIndex(self):
        if self.scores['word_count'] != 0:
            difficultwords = self.scores['word_count'] - self.scores['simpleword_count']
            difficultwords_perc = difficultwords / self.scores['word_count'] * 100
            self.readingindex = (0.1579 * difficultwords_perc) + (0.0496 * self.scores['sentlen_average'])

            if difficultwords_perc > 5:
                self.readingindex = self.readingindex + 3.6365

    def setGrade(self):
        """
        The grade calculation is based on the one in the
        documentation, also allowing for ranges within the
        grades.  The grade calculation counts on after the
        college graduate grade (16), result might be less
        reliable after that.
        """
        if self.readingindex <= 5.9:
            self.us_grade = self.readingindex
        elif self.readingindex > 5.9 and self.readingindex <= 6.9:
            self.us_grade = self.readingindex + 1
        elif self.readingindex > 6.9 and self.readingindex <= 7.9:
            self.us_grade = self.readingindex + 2
        elif self.readingindex > 7.9 and self.readingindex <= 8.9:
            self.us_grade = self.readingindex + 3
        elif self.readingindex > 8.9 and self.readingindex <= 9.9:
            self.us_grade = self.readingindex + 4 + (self.readingindex - int(self.readingindex))
        else:
            self.us_grade = self.readingindex + 6
