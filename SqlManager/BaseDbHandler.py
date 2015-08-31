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

	@abstractmethod
	def CreateTable(self, tableName, tableFields): pass

	@abstractmethod
	def DeleteTable(self, tableName): pass

	@abstractmethod
	def InsertRecord(self, tableName, fields, values): pass

	@abstractmethod
	def SelectAll(self, tableName): pass

	def _executeSqlCommand(self, sqlCommand, fetch=False): pass
