This is a readability calculator library for Python.

You're able to calculate the readability of a text using several algorithms:
 - Flesch-Kincaid
 - Coleman-Liau
 - Dale-Chall
 - SMOG
 - Automated Readability Index
 - Flesch Reading Ease (does not have min_age)

Dutch:
 - Flesch-Douma
 - KPC (AVI)


All available calculators have a min_age property which describes the typical minimum age for a potential reader.

Although the algorithms themselves might not be language independent, they can be called as such using a custom locale. This locale has to be available in the pyphen dependency. By default, the locale is set to 'en_GB'.


Wim Muskee, 2012-2017
wimmuskee@gmail.com

License: GPL-2


# Dependencies
 - NLTK
 - Pyphen
 - Python, tested on 2.7 and 3.4


# Example:
from readability_score.calculators.fleschkincaid import *
from readability_score.calculators.dalechall import *

fk = FleschKincaid(open('/tmp/text.txt').read(), locale='nl_NL')
dc = DaleChall(open( '/tmp/text.txt' ).read(), simplewordlist=awordlist, locale='de_DE')

print(fk.min_age)
print(dc.min_age)


# Tests
Some tests are included with the library. I'am not sure how reactive the scores will be using different dependencies on other systems.
This is not exact science, don't use these tests for anything important.

cd readability_score
python -m unittest discover -s test -v
