# -*- coding: utf-8 -*-
"""
This module contains common functions used
in the various readability calculations.

Wim Muskee, 2012-2017
wimmuskee@gmail.com

License: GPL-2
"""
from __future__ import division

def getTextScores(text, locale='en_GB', simplewordlist=[]):
    """
    Calculates several text scores based on a piece of text.
    A custom locale can be provided for the hyphenator, which
    maps to a Myspell hyphenator dictionary.  If the locale
    is a file descriptor or file path the dictionary at that
    path will be used instead of those in the default Myspell
    location.
    The simple word list should be provided in lower case. 
    """
    from sys import version_info
    from nltk.tokenize import sent_tokenize, word_tokenize
    import pyphen
    import re
    import os

    # check if locale is supported
    if locale not in pyphen.LANGUAGES:
        raise LookupError("provided locale not supported by pyphen")

    hyphenator = pyphen.Pyphen(lang=locale)

    scores = {
              'sent_count': 0,              # nr of sentences
              'word_count': 0,              # nr of words
              'letter_count':0,             # nr of characters in words (no spaces)
              'syll_count': 0,              # nr of syllables
              'polysyllword_count': 0,      # nr of polysyllables (words with more than 3 syllables)
              'simpleword_count': 0,        # nr of simplewords (depends on provided list)
              'sentlen_average': 0,         # words per sentence
              'wordlen_average': 0,         # syllables per word
              'wordletter_average': 0,      # letters per word
              'wordsent_average': 0         # sentences per word
              }

    if version_info.major == 2:
        if isinstance(text,unicode):
            sentences = sent_tokenize(text)
        else:
            sentences = sent_tokenize(unicode(text,'utf-8'))
    elif version_info.major >= 3:
        sentences = sent_tokenize(text)
    else:
        raise RuntimeError("Python version too low")

    scores['sent_count'] = len(sentences)

    for s in sentences:
        words = re.findall(r'\w+', s, flags = re.UNICODE)
        scores['word_count'] = scores['word_count'] + len(words)

        for w in words:
            syllables_count = hyphenator.inserted(w).count('-') + 1
            scores['letter_count'] = scores['letter_count'] + len(w)
            scores['syll_count'] = scores['syll_count'] + syllables_count

            if syllables_count > 2:
                scores['polysyllword_count'] = scores['polysyllword_count'] + 1

            if simplewordlist:
                if w.lower() in simplewordlist:
                    scores['simpleword_count'] = scores['simpleword_count'] + 1


    if scores['sent_count'] > 0:
        scores['sentlen_average'] = scores['word_count'] / scores['sent_count']

    if scores['word_count'] > 0:
        scores['wordlen_average'] = scores['syll_count'] / scores['word_count']
        scores['wordletter_average'] = scores['letter_count'] / scores['word_count']
        scores['wordsent_average'] = scores['sent_count'] / scores['word_count']

    return scores


def getMinimumAgeFromUsGrade(us_grade):
    """
    The age has a linear relation with the grade.
    http://en.wikipedia.org/wiki/Education_in_the_United_States#School_grades
    """
    return int(round(us_grade + 5))

