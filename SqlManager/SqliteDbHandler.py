# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 23:29:20 2015

@author: RedSpiderMkV
"""

import sqlite3 as lite
import os

class DatabaseHandler:
	def __init__(self, DEBUG = False):
		self.__printFlag = DEBUG
		
	def CreateDatabase(self, dbNameWithPath):
		try:
			con = lite.connect(dbNameWithPath)
			self._print('Created database')
			
			return True
		except lite.Error, e:
			self._print(e.message)
		finally:
			con.close()
			
		return False
			
	def SetDatabase(self, dbNameWithPath):
		if os.path.exists(dbNameWithPath):
			try:
				con = lite.connect(dbNameWithPath)
				self._print('Using database')
				
				return True
			except lite.Error, e:
				self._print(e.message)
			finally:
				con.close()
		else:
			self._print('Database doesn\'t exist')
			
		return False
			
	def _print(self, message):
		if self.__printFlag:
			print(message)