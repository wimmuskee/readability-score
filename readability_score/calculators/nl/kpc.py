# -*- coding: utf-8 -*-
"""
This is the KPC AVI readability calculator

This tool can calculate the AVI readability score 
of a Dutch text using the old KPC method.
http://nl.wikipedia.org/wiki/AVI_%28onderwijs%29

Wim Muskee, 2012-2017
wimmuskee@gmail.com

License: GPL-2
"""
from __future__ import division
from readability_score.textanalyzer import TextAnalyzer


class KPC(TextAnalyzer):
	def __init__(self, text, locale='en_GB'):
		TextAnalyzer.__init__(self,text,locale)
		self.setTextScores()
		self.avi = 0
		self.readingindex = 0
		self.setReadingIndex()
		self.setAvi()
		self.setMinimumAge()


	def setReadingIndex(self):
		"""
		Calculates reading index required for AVI calculation.
		Sets readingindex as float.  When using with the avi 
		calculating table, it should be rounded to a whole integer.
		"""	
		self.readingindex = 192 - ( 2 * self.scores['sentlen_average'] ) - ( 200/3 * self.scores['wordlen_average'] )


	def setAvi(self):
		"""
		Calculates AVI level using the old KPC method.  The calculation
		follows the documentation until AVI 9.  However more AVI scores
		will be calculated.
		"""
		readingindex = round(self.readingindex)
		
		if readingindex > 127:
			self.avi = 0
		elif readingindex <= 127 and readingindex >= 123:
			self.avi = 1
		elif readingindex <= 123 and readingindex >= 112:
			self.avi = 2
		elif readingindex <= 120 and readingindex >= 108 and self.scores['wordlen_average'] >= 1.10:
			self.avi = 3
		elif readingindex <= 110 and readingindex >= 100 and self.scores['wordlen_average'] >= 1.15:
			self.avi = 4
		elif readingindex <= 99 and readingindex >= 94:
			self.avi = 5
		else:
			avi = 5
			max_index = 98
			i = 1
			
			while (not self.avi):
				max_index = max_index - 5
				min_index = max_index - 4
				
				if readingindex <= max_index and readingindex >= min_index:
					self.avi = avi + i
					
				i = i + 1
		

	def setMinimumAge(self):
		"""
		Sets minimum age required for reading a text based
		on set AVI score.  The calculation is based roughly on
		the documentation. 
		"""
		if self.avi == 0:
			self.min_age = 0
		elif self.avi < 8:
			self.min_age = int(round( (self.avi/3) + 6 )) 
		else:
			self.min_age = int(round( (self.avi/2) + 5 )) 

