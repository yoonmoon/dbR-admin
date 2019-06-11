import ibm_db
import os


db2cmds = {
	"list.db" : "db2 list db directory | grep 'Database name'",
	"list.all_tab" : "db2 list tables for all",
	"list.all_tbs" : "db2 list tablespaces show detail"
}

db2sqls = {
	"cat.tables" : "select `{columnlist}` from syscat.tables",
	"cat.tables" : "select `{columnlist}` from syscat.tables",
	"cat.columns" : "select `{columnlist}` from syscat.columns",
	"cat.indexes" : "select `{columnlist}` from syscat.indexes",
	"mon.conns" : "select `{columnlist}` from table( MON_GET_CONNECTION(null, -2) ) t"
}

db2look = {
	"schema" : "db2look -d `{database}` -a -e -x -noimplschema -z `{schema}` -o `{fileName}`.sql"
}

def applyField( query, fieldName, value ):
	return query.replace("`{"+fieldName+"}`", value)

def getDb2Look( cmd ):
	return db2look[cmd]

def getSqlByCols( name, columnList ):
	return applyField(db2sqls[name], "columnlist", columnList)


# List of Databases
def getDatabaseList():
	listDb = os.popen(db2cmds['list.db']).read().split('\n')
	dbNames = []
	for i in listDb:
		#print i
		if len(i.split(" = ")) > 1:
			dbNames.append(i.split(" = ")[1])
	return dbNames

def execSql4Obj( conn, sql ):
	result = ibm_db.exec_immediate(conn, sql)
	row = ibm_db.fetch_tuple(result)
	while ( row ):
		#print("%5s  %-10s %5s %-7s %5s %15s %10s " % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
	#	row_str = ""
		for element in row:
			row_str += str(element) +","
		print row
	#	print row_str
		row = ibm_db.fetch_tuple(result)
	return result


def execSql4Str( conn, sql ):
	result = ibm_db.exec_immediate(conn, sql)
	row = ibm_db.fetch_tuple(result)
	while ( row ):
		#print("%5s  %-10s %5s %-7s %5s %15s %10s " % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
		row_str = ""
		for element in row:
			row_str += str(element) +","
	#	print row
		print row_str
		row = ibm_db.fetch_tuple(result)
	return result