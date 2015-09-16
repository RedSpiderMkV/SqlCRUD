
from datetime import datetime
import SqlManager.SqlManager as SqlManager

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
	#testSql(SqlManager.GetSqlHandler(SqlManager.MYSQL, True))
	# Sqlite
	testSql(SqlManager.GetSqlHandler(SqlManager.SQLITE, True))
