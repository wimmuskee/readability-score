# -*- coding: utf-8 -*-
"""
This module contains common functions used
in the various readability calculations.

Wim Muskee, 2012
wimmuskee@gmail.com

License: GPL-2
"""
from __future__ import division

def getTextScores(text):
    """
    Calculates several text scores based on a piece of text.
    """
    from nltk.tokenize import sent_tokenize
    from hyphenator import Hyphenator
    
    hyphenator = Hyphenator("/usr/share/myspell/hyph_nl_NL.dic")
    scores = {
              'sent_count': 0, 
              'word_count': 0,
              'syll_count': 0,
              'sentlen_average': 0,
              'wordlen_average': 0
              }
    
    sentences = sent_tokenize(text)
    scores['sent_count'] = len(sentences)

    for s in sentences:
        words = s.split( ' ' )
        scores['word_count'] = scores['word_count'] + len(words)
            
        for w in words:
            scores['syll_count'] = scores['syll_count'] + hyphenator.inserted(w).count('-') + 1

    scores['sentlen_average'] = scores['word_count'] / scores['sent_count']
    scores['wordlen_average'] = scores['syll_count'] / scores['word_count']
    
    return scores
