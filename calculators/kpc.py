"""
This is the KPC Python AVI calculator

This tool can calculate the AVI score of a Dutch text
using the the old KPC method.
http://nl.wikipedia.org/wiki/AVI_%28onderwijs%29

Wim Muskee, 2012
wimmuskee@gmail.com

License: GPL-2
"""
from __future__ import division
from nltk.tokenize import sent_tokenize
from hyphenator import Hyphenator

class KPC:
	def __init__(self):
		self.avi = 0
		self.readingindex = 0
		self.min_age = 0
		self.sent_count = 0
		self.word_count = 0
		self.syll_count = 0
		self.sent_average = 0
		self.word_average = 0
		self.hyphenator = Hyphenator("/usr/share/myspell/hyph_nl_NL.dic")
		

	def set_avi(self, text):
		"""
		Calculates AVI level using the old KPC method.  The calculation
		follows the documentation until AVI 9.  However more AVI scores
		will be calculated.
		"""
		self.set_kpc_readingindex(text)
		readingindex = round(self.readingindex)
		
		if readingindex <= 127 and readingindex >= 123:
			self.avi = 1
		elif readingindex <= 123 and readingindex >= 112:
			self.avi = 2
		elif readingindex <= 120 and readingindex >= 108 and self.word_average >= 1.10:
			self.avi = 3
		elif readingindex <= 110 and readingindex >= 100 and self.word_average >= 1.15:
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
	

	def set_kpc_readingindex(self, text):
		"""
		Calculates reading index required for AVI calculation.
		Sets readingindex as float.  When using with the avi 
		calculating table, it should be rounded to a whole integer.
		"""	
		
		# gather data
		sentences = sent_tokenize( text )
		self.sent_count = self.sent_count + len( sentences )
		
		for s in sentences:
			words = s.split( ' ' )
			self.word_count = self.word_count + len( words )
			
			for w in words:
				self.syll_count = self.syll_count + self.hyphenator.inserted(w).count('-') + 1
				
	
		# calculate values
		self.sent_average = self.word_count / self.sent_count
		self.word_average = self.syll_count / self.word_count
		self.readingindex = 192 - ( 2 * self.sent_average ) - ( 200/3 * self.word_average )	


	def set_minimum_age(self):
		"""
		Sets minimum age required for reading a text based
		on set AVI score.  The calculation is based roughly on
		the documentation. 
		"""
		if self.avi < 8:
			self.min_age = round( (self.avi/3) + 6 ) 
		else:
			self.min_age = round( (self.avi/2) + 5 ) 

