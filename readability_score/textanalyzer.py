# -*- coding: utf-8 -*-
"""
This class contains the main text analyzer used in all
the calculators.

Wim Muskee, 2012-2017
wimmuskee@gmail.com

License: GPL-2
"""
from __future__ import division
from sys import version_info
import warnings
import re

with warnings.catch_warnings():
    # catch NLTK warning, fixed in 4.2.2
    warnings.filterwarnings("ignore",category=PendingDeprecationWarning,message='the imp module is deprecated in favour of importlib.*')
    # catch ndg-httpsclient warning, fixed in 0.4.2
    warnings.filterwarnings("ignore",category=ImportWarning,message='Not importing directory.*ndg.*')
    # catch matplotlib warning, don't know what the issue is, no problem for this package
    warnings.filterwarnings("ignore",category=ImportWarning,message='Not importing directory.*mpl_toolkits.*')

    from nltk.tokenize import sent_tokenize, word_tokenize
    import pyphen


class TextAnalyzer:
    def __init__(self,text,locale='en_GB'):
        # check if locale is supported
        if len(locale) < 2 or locale not in pyphen.LANGUAGES:
            raise LookupError("provided locale not supported by pyphen")

        self.setText(text)
        self.sentences = []
        self.simple_words = []
        self.min_age = 0
        self.scores = {
            'sent_count': 0,              # nr of sentences
            'word_count': 0,              # nr of words
            'letter_count':0,             # nr of characters in words (no spaces)
            'syll_count': 0,              # nr of syllables
            'polysyllword_count': 0,      # nr of polysyllables (words with more than 2 syllables)
            'simpleword_count': 0,        # nr of simplewords (depends on provided list)
            'sentlen_average': 0,         # words per sentence
            'wordlen_average': 0,         # syllables per word
            'wordletter_average': 0,      # letters per word
            'wordsent_average': 0         # sentences per word
        }
        self.re_words = re.compile(r'\w+', flags = re.UNICODE)
        self.hyphenator = pyphen.Pyphen(lang=locale)


    def setText(self,text):
        """
        Sets the text, and makes sure Python2 is working with unicode.
        """
        if version_info.major == 1:
            raise RuntimeError("Python version too low")
        elif version_info.major == 2 and not isinstance(text,unicode):
            self.text = unicode(text,'utf-8')
        else:
            self.text = text


    def setSimpleWordsList(self,simplewords):
        """
        Simple word list for DaleChall calculator.
        """
        if isinstance(simplewords,list):
            self.simple_words = simplewords
        else:
            raise ValueError("A simple word list should be provided as list")


    def setTextScores(self):
        """
        Wrapper for setting all the scores.
        """
        self.setSentences()
        self.parseSentences()
        self.setAverages()


    def setSentences(self):
        """
        Tokenize the sentences from the text.
        """
        self.sentences = sent_tokenize(self.text)
        self.scores['sent_count'] = len(self.sentences)


    def parseSentences(self):
        """
        Parse each sentence and each word, and count
        the individual countable scores.
        """
        for s in self.sentences:
            words = self.re_words.findall(s)
            self.scores['word_count'] += len(words)

            for w in words:
                syllables_count = self.hyphenator.inserted(w).count('-') + 1
                self.scores['syll_count'] += syllables_count
                self.scores['letter_count'] += len(w)

                if syllables_count > 2:
                    self.scores['polysyllword_count'] += 1

                if self.simple_words:
                    if w.lower() in self.simple_words:
                        self.scores['simpleword_count'] += 1


    def setAverages(self):
        """
        Sets all relevant averages based on the
        individual counts.
        """
        if self.scores['sent_count'] > 0:
            self.scores['sentlen_average'] = self.scores['word_count'] / self.scores['sent_count']

        if self.scores['word_count'] > 0:
            self.scores['wordlen_average'] = self.scores['syll_count'] / self.scores['word_count']
            self.scores['wordletter_average'] = self.scores['letter_count'] / self.scores['word_count']
            self.scores['wordsent_average'] = self.scores['sent_count'] / self.scores['word_count']
