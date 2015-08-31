# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:00:49 2015

@author: RedSpiderMkV
"""

from abc import ABCMeta, abstractmethod

class DbHandler(object):
	_metaclass_ = ABCMeta	
	
	def __init__(self, DEBUG=False):
		self._printFlag = DEBUG
		
	@abstractmethod
	def CreateDatabase(self, dbName): pass

	@abstractmethod
	def DeleteDatabase(self, dbName): pass

	@abstractmethod
	def SetDatabase(self, dbName): pass

	def CreateTable(self, tableName, tableFields):
		sqlCommand = "CREATE TABLE IF NOT EXISTS " + tableName + "("
		
		for field in tableFields:
			sqlCommand += field[0] + " " + field[1] + ","
			
		sqlCommand = self._appendClosingBrace(sqlCommand)
		self._executeSqlCommand(sqlCommand)
		
	def DeleteTable(self, tableName):
		sqlCommand = "DROP TABLE IF EXISTS " + tableName
		self._executeSqlCommand(sqlCommand)

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

	def _executeSqlCommand(self, sqlCommand, fetch=False): pass

	def _appendClosingBrace(self, sqlCommand):
		sqlCommand = sqlCommand[0:len(sqlCommand) - 1]
		sqlCommand += ")"
		
		return sqlCommand	

	def _print(self, message):
		if self._printFlag:
			print(message)
