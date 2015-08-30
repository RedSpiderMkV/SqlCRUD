
import MySQLdb as db

class DatabaseHandler:
	def __init__(self, credentials, DEBUG=False):
		self.__credentials = credentials
		self.printFlag = DEBUG
		
	def OpenConnection(self):
		self.dbConnection = db.connect(self.__credentials.Host, \
							   self.__credentials.User, \
							   self.__credentials.Password, '')
	
	def CloseConnection(self):
		self.dbConnection.close()
		self._printMessage('Connection closed')
	
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

	def CreateTable(self, tableName, tableFields):
		sqlCommand = "CREATE TABLE IF NOT EXISTS " + tableName + "("
		
		for field in tableFields:
			sqlCommand += field[0] + " " + field[1] + ","
			
		sqlCommand = self._appendClosingBrace(sqlCommand)
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
		
		if self._executeSqlCommand(sqlCommand):
			self.dbConnection.commit()
		else:
			self.dbConnection.rollback()	
		
	def DeleteTable(self, tableName):
		sqlCommand = "DROP TABLE " + tableName
		self._executeSqlCommand(sqlCommand)
		
	def SelectAll(self, tableName):
		sqlCommand = "SELECT * FROM " + tableName
		
		cursor = self.dbConnection.cursor()
		cursor.execute(sqlCommand)
		
		data = cursor.fetchall()
		
		for row in data:
			print row

	def _appendClosingBrace(self, sqlCommand):
		sqlCommand = sqlCommand[0:len(sqlCommand) - 1]
		sqlCommand += ")"
		
		return sqlCommand

	def _executeSqlCommand(self, command):
		try:
			cursor = self.dbConnection.cursor()
			cursor.execute(command)
			cursor.close()
			
			self._printMessage('command executed successfully')
			
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

	def _printMessage(self, msg):
		if self.printFlag:
			print(msg)
