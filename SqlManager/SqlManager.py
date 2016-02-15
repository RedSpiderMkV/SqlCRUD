# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:58:54 2015

@author: RedSpiderMkV
"""

from DatabaseHandler.MySqlDbHandler import MySqlHandler
from DatabaseHandler.SqliteDbHandler import SqliteHandler

class SqlManager:
    SQLITE = 0
    MYSQL = 1

    def __init__(self, credentialFile):
        self.__credentialFile = credentialFile
        
    def GetSqlHandler(self, handlerType, DEBUG=False):
    	if handlerType == self.SQLITE:
    		return SqliteHandler(DEBUG)
    	elif handlerType == self. MYSQL:
    		return MySqlHandler(DEBUG)
