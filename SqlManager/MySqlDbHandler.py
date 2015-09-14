# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 21:12:33 2015

@author: RedSpiderMkV
"""

import MySQLdb as db
import os

from BaseDbHandler import DbHandler
from CredentialManager.CredentialHandler import CredentialHandler

class MySqlHandler(DbHandler):
	def __init__(self, DEBUG=False, credentialsPath=''):
		super(MySqlHandler, self).__init__(DEBUG)
		
		if credentialsPath == '':
			self.__credentials = CredentialHandler('credentials.xml').Credentials
		else:
			self.__credentials = CredentialHandler(os.path.abspath(credentialsPath)).Credentials
		self._openConnection()

	def Dispose(self):
		self._closeConnection()
	
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

	def _openConnection(self):
		self.dbConnection = db.connect(self.__credentials.Host, \
							   self.__credentials.User, \
							   self.__credentials.Password, '')
	
	def _closeConnection(self):
		self.dbConnection.close()
		self._print('Connection closed')

	def _executeSqlCommand(self, command, fetch=False):
		try:
			cursor = self.dbConnection.cursor()
			cursor.execute(command)
			
			self._print('Command executed successfully')
			
			if fetch:
				return cursor.fetchall()
			else:
				self.dbConnection.commit()
				
			return True
		except db.Error, e:
			print('command failed...' + e.args[1])
			
			if not fetch:
				self.dbConnection.rollback()
			
			return False
		finally:
			if cursor:
				try:
					cursor.close()
				except Exception, e:
					print(e.args[1])
