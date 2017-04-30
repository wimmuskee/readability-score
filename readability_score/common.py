# -*- coding: utf-8 -*-
"""
This module contains common functions used
in the various readability calculations.

Wim Muskee, 2012-2017
wimmuskee@gmail.com

License: GPL-2
"""

def getMinimumAgeFromUsGrade(us_grade):
    """
    The age has a linear relation with the grade.
    http://en.wikipedia.org/wiki/Education_in_the_United_States#School_grades
    """
    return int(round(us_grade + 5))
