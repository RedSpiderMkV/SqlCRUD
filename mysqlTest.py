
import sys
sys.path.append('../CredentialManager')

from datetime import datetime
from SqlManager.MySqlDbHandler import DatabaseHandler
from CredentialManager.CredentialHandler import CredentialHandler
import os

from SqlManager.SqliteDbHandler import DatabaseHandler

def test():
	#databaseHandler = DatabaseHandler.OpenWithFile('../CredentialManager/credentials.xml', True)
	
#	credentialsHandler = CredentialHandler(os.path.abspath('credentials.xml'))
#
#	databaseHandler = DatabaseHandler(credentialsHandler.Credentials, True)
#	databaseHandler.OpenConnection()
#	
#	databaseHandler.CreateDatabase('testDb123')
#	databaseHandler.SetDatabase('testDb123')
#	
#	name = 'table1'
#	fields = [('field1', 'VARCHAR(50)'), ('field2', 'INTEGER'), ('timestamp', 'BIGINT')]
#	
#	databaseHandler.CreateTable(name, fields)
#	
#	dateTime = int(datetime.strptime('01-01-2010 10:00:00', '%d-%m-%Y %H:%M:%S').strftime('%s'))
#	
#	fields = ['field1', 'field2', 'timestamp']
#	values = [['"hello"', 15, dateTime], ['"byebye"', 10, dateTime]]
#	databaseHandler.InsertRecord(name, fields, values[0])
#	databaseHandler.InsertRecord(name, fields, values[1])
#	
#	databaseHandler.SelectAll(name)
#	databaseHandler.DeleteTable(name)
#	databaseHandler.DeleteDatabase('testDb123')
#	databaseHandler.CloseConnection()

	databaseHandler = DatabaseHandler(True)
	databaseHandler.CreateDatabase('testDb.db')
	databaseHandler.CreateDatabase('testDb2.db')
	databaseHandler.SetDatabase('testDb.db')
	databaseHandler.DeleteDatabase('testDb.db')

test()
