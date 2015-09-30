
import sys
sys.path.append('../CredentialManager')

from datetime import datetime
from SqlManager.MySqlDbHandler import MySqlHandler
from SqlManager.SqliteDbHandler import SqliteHandler
from CredentialManager.CredentialHandler import CredentialHandler
import os

credentialsHandler = CredentialHandler(os.path.abspath('credentials.xml'))

name = 'table1'
fields = [('field1', 'VARCHAR(50)'), ('field2', 'INTEGER'), ('timestamp', 'BIGINT')]

dateTime = int(datetime.strptime('01-01-2010 10:00:00', '%d-%m-%Y %H:%M:%S').strftime('%s'))
insertFields = ['field1', 'field2', 'timestamp']
insertValues = [['"hello"', 15, dateTime], ['"byebye"', 10, dateTime], ['"hi"', 20, dateTime], ['"boo"', 25, dateTime]]

def testSql(databaseHandler):
	databaseHandler.CreateDatabase('testDb123')
	databaseHandler.SetDatabase('testDb123')
	
	databaseHandler.CreateTable(name, fields)
	
	databaseHandler.InsertRecord(name, insertFields, insertValues[0])
	databaseHandler.InsertRecord(name, insertFields, insertValues[1])
	databaseHandler.InsertManyRecords(name, insertFields, insertValues)
	
	databaseHandler.SelectAll(name)
	databaseHandler.DeleteTable(name)
	databaseHandler.DeleteDatabase('testDb123')
	
	databaseHandler.Dispose()

if __name__ == "__main__":
	# MySql
	testSql(MySqlHandler(credentialsHandler.Credentials, True))
	# Sqlite
	testSql(SqliteHandler(True))
