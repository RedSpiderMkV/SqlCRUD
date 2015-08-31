# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 23:29:20 2015

@author: RedSpiderMkV
"""

import sqlite3 as lite
import os

class DatabaseHandler:
	def __init__(self, DEBUG=False):
		self.__printFlag = DEBUG
		
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
	
	# need commt/rollback
	def CreateTable(self, tableName, tableFields):
		sqlCommand = "CREATE TABLE IF NOT EXISTS " + tableName + "("
		
		for field in tableFields:
			sqlCommand += field[0] + " " + field[1] + ","
			
		sqlCommand = self._appendClosingBrace(sqlCommand)
		self._executeSqlCommand(sqlCommand)
		
	# need commt/rollback
	def DeleteTable(self, tableName):
		sqlCommand = "DROP TABLE IF EXISTS " + tableName
		self._executeSqlCommand(sqlCommand)

	# need commt/rollback		
	def InsertRecord(self, tableName, fields, values):
		sqlCommand = "INSERT INTO " + tableName + "("
		for field in fields:
			sqlCommand += field + ","
			
		sqlCommand = self._appendClosingBrace(sqlCommand)
		
		sqlCommand += "VALUES("
		for value in values:
			sqlCommand += str(value) + ","
			
		sqlCommand = self._appendClosingBrace(sqlCommand)
		
		self._executeSqlCommand(sqlCommand)

	def SelectAll(self, tableName):
		sqlCommand = "SELECT * FROM " + tableName
		
		data = self._executeSqlCommand(sqlCommand, True)
		
		for row in data:
			print row

	def _executeSqlCommand(self, sqlCommand, fetch=False):
		con = lite.connect(self.__dbName)
		with con:
			cur = con.cursor()
			cur.execute(sqlCommand)
			
			if fetch:
				rows = cur.fetchall()
				return rows

	def _appendClosingBrace(self, sqlCommand):
		sqlCommand = sqlCommand[0:len(sqlCommand) - 1]
		sqlCommand += ")"
		
		return sqlCommand	
	
	def _connectToDatabase(self, dbNameWithPath):
		try:
			con = lite.connect(dbNameWithPath)			
			return True
		except lite.Error, e:
			self._print(e.message)
		finally:
			con.close()
			
		return False
			
	def _print(self, message):
		if self.__printFlag:
			print(message)