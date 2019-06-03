import ibm_db
import os

# List of Databases

def getDatabaseList():
	db2list = os.popen("db2 list db directory | grep 'Database name'").read().split('\n')
	databases = []
	for i in db2list:
		#print i
		if len(i.split(" = ")) > 1:
			databases.append(i.split(" = ")[1])
	return databases
