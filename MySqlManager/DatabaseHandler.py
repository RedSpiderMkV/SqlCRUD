
import MySQLdb as db
from CredentialHandler import CredentialHandler

class DatabaseHandler:
	@classmethod
	def OpenWithFile(self, credentialFile, printFlag):
		credentials = CredentialHandler(credentialFile)
		self.printFlag = printFlag
		return self._openConnection(credentials.host, credentials.user, credentials.password, '')
	
	@classmethod
	def OpenWithCredentials(self, host, user, password, database):
		return self._openConnection(host, user, password, database)
	
	def CloseConnection(self):
		self.dbConnection.close()
		
		if self.printFlag:
			print('Connection closed')
	
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
		self._executeSqlCommand(sqlCommand)
		
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

	@classmethod
	def _openConnection(self, host, user, password, database):
		self.dbConnection = db.connect(host, user, password, database)
		
		if self.printFlag:
			print('Connection open')
		
		handler = DatabaseHandler()
		return handler

	def _appendClosingBrace(self, sqlCommand):
		sqlCommand = sqlCommand[0:len(sqlCommand) - 1]
		sqlCommand += ")"
		
		return sqlCommand

	def _executeSqlCommand(self, command):
		try:
			cursor = self.dbConnection.cursor()
			cursor.execute(command)
			cursor.close()
			
			if self.printFlag:
				print('command executed successfully')
		except db.Error, e:
			print('command failed...' + e.args[1])
		finally:
			if cursor:
				try:
					cursor.close()
				except Exception, e:
					print(e.args[1])
