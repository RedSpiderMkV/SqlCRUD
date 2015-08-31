# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 21:12:33 2015

@author: RedSpiderMkV
"""

import MySQLdb as db

from BaseDbHandler import DbHandler

class MySqlHandler(DbHandler):
	def __init__(self, credentials, DEBUG=False):
		super(MySqlHandler, self).__init__(DEBUG)
		self.__credentials = credentials
		
	def OpenConnection(self):
		self.dbConnection = db.connect(self.__credentials.Host, \
							   self.__credentials.User, \
							   self.__credentials.Password, '')
	
	def CloseConnection(self):
		self.dbConnection.close()
		self._print('Connection closed')
	
	def SetDatabase(self, dbName):
		self.dbName = dbName
		sqlCommand = "USE " + dbName
		self._executeSqlCommand(sqlCommand)
	
	def CreateDatabase(self, dbName):
		sqlCommand = "CREATE DATABASE IF NOT EXISTS " + dbName
		self._executeSqlCommand(sqlCommand)
		
	def DeleteDatabase(self, dbName):
		sqlCommand = "DROP DATABASE " + dbName
		self._executeSqlCommand(sqlCommand)

	def _executeSqlCommand(self, command, fetch=False):
		try:
			cursor = self.dbConnection.cursor()
			cursor.execute(command)
			
			self._print('command executed successfully')
			
			if fetch:
				return cursor.fetchall()
				
			return True
		except db.Error, e:
			print('command failed...' + e.args[1])
			
			return False
		finally:
			if cursor:
				try:
					cursor.close()
				except Exception, e:
					print(e.args[1])
