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
    if us_grade == 0:
        return 0

    from decimal import Decimal, ROUND_HALF_UP
    min_age = int(Decimal(us_grade + 5).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    if min_age < 0:
        return 0
    else:
        return min_age
