from db2 import event_mon
from db2 import db2_info
import ibm_db
import sys
import os
from common import shell_ext
from common import config
import readline
import db2_env



#db2_env
#config.saveSecret()
#print config.getSecret()

#print db2_info.getSqlByCols('cat.tables', '*')
#print db2_info.getSqlByCols('mon.conns', '*')

##os.environ['DBR_MODULE']='testing module'

em = db2_env.mappings
print " +env.mappings : ", em
## Check Presets
action = os.getenv(em['action'])
if ( action == None ):
	action = raw_input('Enter Your Action: ')

conn = ibm_db.connect(os.getenv(em['database']), os.getenv(em['user']), config.getSecret() )

if action == 'sql':
	tabName = raw_input( "tabName: ")
	columnList = raw_input( "columnList: ")
	whereClause = str(raw_input( "whereClause: "))
	if ( whereClause != None or whereClause != '' ): 
		whereClause += "WHERE "+ whereClause
	print db2_info.execSql4Str( conn, db2_info.getSqlByCols('cat.tables', columnList) )

if action == 'look.schema':
	dbName = os.getenv(em['database'])
	if dbName == None:
		dbName = raw_input( "Database: ")
	
	schema = os.getenv(em['schema'])
	if ( schema == None ):
		schema = raw_input( "Schema: ")
	
	#fileName = raw_input( "FileName: ")
	cmd = db2_info.getDb2Look("schema")
	cmd = db2_info.applyField(cmd, "database", dbName)
	cmd = db2_info.applyField(cmd, "schema", schema)
	#cmd = db2_info.applyField(cmd, "fileName", fileName)
	print(cmd)
	db2lookData = os.popen(cmd).read()
	print db2_info.applyRemoveSchema( db2lookData, schema )

if action == 'listEM':
	event_mon.listEventMon( conn )

if action == 'enable':
	event_mon.enableDefaultClass( conn )

if action == 'creatEM':
	event_mon.createEventMon( conn, 'TEST1', '', '' )

if action == 'selectEM':
	event_mon.selectEventMon( conn, evmonName )

if action == 'dropEM':
	event_mon.dropEventMon( conn, 'CONN_DB_APPLS', '', '' )

ibm_db.close(conn)
