# -*- coding: utf-8 -*-
"""
This is the SMOG readability calculator

This tool can calculate the readability score of a text
using the Simple Measure Of Gobbledygook.
For texts with 30 or more sentences, the calculator gets a sample
of 10 sentences from the beginning, middle and the end of the text.

http://en.wikipedia.org/wiki/SMOG_%28Simple_Measure_Of_Gobbledygook%29
http://webpages.charter.net/ghal/SMOG_Readability_Formula_G._Harry_McLaughlin_%281969%29.pdf

Wim Muskee, 2012-2017
wimmuskee@gmail.com

https://github.com/i-trofimtschuk, 2013

License: GPL-2
"""
from __future__ import division
from readability_score.common import getMinimumAgeFromUsGrade
from readability_score.textanalyzer import TextAnalyzer


class SMOG(TextAnalyzer):
    def __init__(self, text, locale='en_GB'):
        TextAnalyzer.__init__(self,text,locale)
        self.setTextScores()
        self.us_grade = 0
        self.setGrade()
        self.min_age = getMinimumAgeFromUsGrade(self.us_grade)

    def setTextScores(self):
        """
        SMOG custom wrapper for setting all the scores.
        """
        self.setSentences()
        if self.scores["sent_count"] >= 30:
            sentence_middle = int(self.scores["sent_count"]/2)
            self.sentences = self.sentences[:10] + self.sentences[sentence_middle -5:5+ sentence_middle] + self.sentences[-10:]
            self.scores["sent_count"] = len(self.sentences)
        self.parseSentences()
        self.setAverages()

    def setGrade(self):
        """
        Calculates US grade as a float from the available
        text scores.
        """
        if self.scores['sent_count'] != 0:
            self.us_grade = (1.043 * ((self.scores['polysyllword_count'] * (30 / self.scores['sent_count']))**0.5)) + 3.1291
