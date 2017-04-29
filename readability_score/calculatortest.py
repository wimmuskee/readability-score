# -*- coding: utf-8 -*-

# class used by each calculator test
class CalculatorTest():
    def __init__(self,min_test_age):
        self.text = "Readability is the ease with which a reader can understand a written text. In natural language, the readability of text depends on its content (the complexity of its vocabulary and syntax) and its presentation (such as typographic aspects like font size, line height, and line length)."
        self.text_ro = "Lizibilitatea (etimologie franceză lisibilité) este calitatea unui text de a fi ușor de citit și înțeles. De-a lungul timpului, au fost dezvoltate mai multe criterii pentru evaluarea lizibilității. Unul dintre acestea este viteza de citire. Lizibilitatea a fost cercetată în amănunțime în secolul al XX-lea, fiind elaborate mai multe sisteme de ameliorare a lizibilității textelor."
        self.min_age_test = min_test_age
        self.test_range = [ self.min_age_test, self.min_age_test + 1, self.min_age_test - 1 ]
        self.test_range_fail_text = "min_age is not within 1 year range of " + str(self.min_age_test)
