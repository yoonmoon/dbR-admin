import ibm_db
import db2_sql
import string
import sys



evMons = {'ACTIVITIES'}

def getEventMonitors():
	return evMons

def enableDefaultClass( conn ):
	if conn:		
		#sql = "create table test1( col1 int, col2 varchar(100) )"
		sql = "alter service class sysdefaultsubclass under sysdefaultuserclass collect activity data on all database partitions with details and values"
		try:
			stmt = ibm_db.exec_immediate(conn, sql)	
		except:
			print "enableDefaultClass() couldn't be completed:" , ibm_db.stmt_errormsg()
		else:
			print "enableDefaultClass() complete.", ibm_db.stmt_errormsg()

def listEventMon( conn ):
	result = ibm_db.exec_immediate(conn, "select * from SYSCAT.EVENTMONITORS with ur")
	row = ibm_db.fetch_tuple(result)
	while ( row ):
		#print("%5s  %-10s %5s %-7s %5s %15s %10s " % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
		row_str = ""
		for element in row:
			row_str += str(element) +","
		print row
		print row_str
		row = ibm_db.fetch_tuple(result)


def createEventMon( conn, evmonName, type, filter ):
	if conn:
		server = ibm_db.server_info( conn )
		print server		
		#sql = "create table test1( col1 int, col2 varchar(100) )"
		sql = "create event monitor EM_"++" for "++" write to table manualstart"
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
		#sql = "create table test1( col1 int, col2 varchar(100) )"
		sql = "DROP EVENT MONITOR "+evmonName+" FOR CONNECTIONS"
		try:
			stmt = ibm_db.exec_immediate(conn, sql)	
		except:
			print "Transaction couldn't be completed:" , ibm_db.stmt_errormsg()
		else:
			print "Transaction complete."

def selectEventMon( conn, evmonName ):
	if conn:
		sql = db2_sql.setParameter("select * from SYSCAT.EVENTMONITORS where EVMONNAME like {evmonname} with ur", 'evmonname', evmonName)
		print sql
		stmt = ibm_db.prepare(conn, sql )
		if ibm_db.execute(stmt):
			row = ibm_db.fetch_tuple(stmt)
			while ( row ):
				print row
				for i in row:
					#print(i)
					row = ibm_db.fetch_tuple(stmt)
	else:
		print("Connection failed.")

