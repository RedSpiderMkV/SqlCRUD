
from xml.dom import minidom

class CredentialHandler:
	HOSTFIELD = 'host'
	USERFIELD = 'user'
	PASSWORDFIELD = 'password'
	CREDENTIALFILENAME = ''
	
	def __init__(self, credentialFile):
		self.CREDENTIALFILENAME = credentialFile
		xmldoc = minidom.parse(self.CREDENTIALFILENAME)
		
		self.host = xmldoc.getElementsByTagName(self.HOSTFIELD)[0].firstChild.nodeValue
		self.user = xmldoc.getElementsByTagName(self.USERFIELD)[0].firstChild.nodeValue
		self.password = xmldoc.getElementsByTagName(self.PASSWORDFIELD)[0].firstChild.nodeValue

