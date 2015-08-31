# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:00:49 2015

@author: RedSpiderMkV
"""

class DbHandler(object):
	def __init__(self, DEBUG=False):
		self._printFlag = DEBUG