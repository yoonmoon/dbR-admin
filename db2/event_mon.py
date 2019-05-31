import ibm_db
import string
import sys


def createEventMon( conn, evmonName, type, filter ):
	if conn:
		server = ibm_db.server_info( conn )
		print server
		result = ibm_db.columns(conn,None,None,"EMPLOYEE")
		row = ibm_db.fetch_both(result)
		print row		
		#sql = "create table test1( col1 int, col2 varchar(100) )"
		sql = "CREATE EVENT MONITOR "+evmonName+" FOR CONNECTIONS write to table"
		try:
			stmt = ibm_db.exec_immediate(conn, sql)	
		except:
			print "Transaction couldn't be completed:" , ibm_db.stmt_errormsg()
		else:
			print "Transaction complete."

def dropEventMon( conn, evmonName, type, filter ):
	if conn:
		server = ibm_db.server_info( conn )
		print server
		result = ibm_db.columns(conn,None,None,"EMPLOYEE")
		row = ibm_db.fetch_both(result)
		print row		
		#sql = "create table test1( col1 int, col2 varchar(100) )"
		sql = "DROP EVENT MONITOR "+evmonName+" FOR CONNECTIONS"
		try:
			stmt = ibm_db.exec_immediate(conn, sql)	
		except:
			print "Transaction couldn't be completed:" , ibm_db.stmt_errormsg()
		else:
			print "Transaction complete."

def selectEventMon( conn, evmonName, type, filter ):
	if conn:
		stmt = ibm_db.prepare(conn, "SELECT * FROM "+evmonName)
		if ibm_db.execute(stmt):
			row = ibm_db.fetch_tuple(stmt)

			while ( row ):
				print row
				for i in row:
					#print(i)
					row = ibm_db.fetch_tuple(stmt)
	else:
		print("Connection failed.")

def printMsg( message ):
	print message
	return message

