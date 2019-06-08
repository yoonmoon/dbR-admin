from os.path import expanduser
import os
import pickle


def saveSecret():
	password = raw_input('Enter Password: ')
	homePath = expanduser("~")
	filePath = os.path.join(homePath, ".dbR_config")
	print "filePath=", filePath
	dict={'dbR_password': str(password)}
	file = open( filePath, 'w')
	pickle.dump(dict, file)
	file.close()
	return dict['dbR_password']

def getSecret():
	homePath = expanduser("~")
	print "homePath=", homePath
	filePath = os.path.join(homePath, ".dbR_config")
	file = open( filePath, 'r')
	dict = pickle.load(file)
	file.close()
	return dict['dbR_password']


