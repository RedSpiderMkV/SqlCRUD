# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 23:29:20 2015

@author: RedSpiderMkV
"""

import sqlite3 as lite
import os

from BaseDbHandler import DbHandler

class SqliteHandler(DbHandler):
	def __init__(self, DEBUG=False):
		super(SqliteHandler, self).__init__(DEBUG)
		
	def CreateDatabase(self, dbNameWithPath):
		if self._connectToDatabase(dbNameWithPath):
			self.__dbName = dbNameWithPath
			self._print('Created database')
			return True
			
		return False

	def DeleteDatabase(self, dbNameWithPath):
		os.remove(dbNameWithPath)
		
		if not os.path.exists(dbNameWithPath):
			self._print('Database deleted')
			return True
		
		return False
	
	def SetDatabase(self, dbNameWithPath):
		if os.path.exists(dbNameWithPath):
			if self._connectToDatabase(dbNameWithPath):
				self.__dbName = dbNameWithPath
				self._print('Using database')
				return True
		else:
			self._print('Database doesn\'t exist')
			
		return False

	def _executeSqlCommand(self, sqlCommand, fetch=False):
		con = lite.connect(self.__dbName)
		with con:
			cur = con.cursor()
			cur.execute(sqlCommand)
			
			self._print("command executed successfully")
			
			if fetch:
				rows = cur.fetchall()
				return rows
	
	def _connectToDatabase(self, dbNameWithPath):
		try:
			con = lite.connect(dbNameWithPath)			
			return True
		except lite.Error, e:
			self._print(e.message)
		finally:
			con.close()
			
		return False
