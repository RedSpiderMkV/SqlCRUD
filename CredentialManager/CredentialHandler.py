
import sys
sys.path.append('../CredentialStore')

from xml.dom import minidom
from CredentialStore.CredentialStore import CredentialStore

class CredentialHandler:
	__HOSTFIELD = 'host'
	__USERFIELD = 'user'
	__PASSWORDFIELD = 'password'
	
	def __init__(self, credentialFile):
		xmldoc = minidom.parse(credentialFile)
		
		host = xmldoc.getElementsByTagName(self.__HOSTFIELD)[0].firstChild.nodeValue
		user = xmldoc.getElementsByTagName(self.__USERFIELD)[0].firstChild.nodeValue
		password = xmldoc.getElementsByTagName(self.__PASSWORDFIELD)[0].firstChild.nodeValue
		
		self.Credentials = CredentialStore(host, user, password)
