# -*- coding: utf-8 -*-
"""
This is the Flesch-Douma readability calculator

This tool can calculate the readability score of a text
using the Flesch-Douma index.
http://www.kennislink.nl/publicaties/hoe-begrijpelijk-is-mijn-tekst
http://hchiemstra.wordpress.com/2011/02/24/is-de-leesbaarheid-van-een-tekst-objectief-te-meten/

Wim Muskee, 2012-2017
wimmuskee@gmail.com

License: GPL-2
"""
from readability_score.textanalyzer import TextAnalyzer


class FleschDouma(TextAnalyzer):
    def __init__(self, text, locale='en_GB'):
        TextAnalyzer.__init__(self,text,locale)
        self.setTextScores()
        self.readingindex = 0
        self.setReadingIndex()
        self.setMinimumAge()

    def setReadingIndex(self):
        self.readingindex = 206.84 - (0.77 * self.scores['sentlen_average']) - (93 * self.scores['wordlen_average'])

    def setMinimumAge(self):
        """
        Mapped the textual descriptions of the target groups
        on to ages. Extrapolated this beyond the index of 100.
        """
        if self.readingindex < 30:
            self.min_age = 24
        elif self.readingindex >= 30 and self.readingindex < 50:
            self.min_age = 18
        elif self.readingindex >= 50 and self.readingindex < 60:
            self.min_age = 16
        elif self.readingindex >= 60 and self.readingindex < 70:
            self.min_age = 12
        elif self.readingindex >= 70 and self.readingindex < 80:
            self.min_age = 11
        elif self.readingindex >= 80 and self.readingindex < 90:
            self.min_age = 10
        elif self.readingindex >= 90 and self.readingindex < 100:
            self.min_age = 9
        # extrapolated from this point
        elif self.readingindex >= 100 and self.readingindex < 110:
            self.min_age = 8
        elif self.readingindex >= 110 and self.readingindex < 120:
            self.min_age = 7
        else:
            self.min_age = 6
