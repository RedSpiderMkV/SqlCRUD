# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:58:54 2015

@author: RedSpiderMkV
"""

from DatabaseHandler.MySqlDbHandler import MySqlHandler
from DatabaseHandler.SqliteDbHandler import SqliteHandler

SQLITE = 0
MYSQL = 1

def GetSqlHandler(handlerType, DEBUG=False):
	if handlerType == SQLITE:
		return SqliteHandler(DEBUG)
	elif handlerType == MYSQL:
		return MySqlHandler(DEBUG)
