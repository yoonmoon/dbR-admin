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

action = raw_input('Enter Your Action: ')

em = db2_env.mappings
print em
print " +executing...", action
conn = ibm_db.connect(os.getenv(em['database']), os.getenv(em['user']), config.getSecret() )

if action == 'sql':
	tabName = raw_input( "tabName: ")
	columnList = raw_input( "columnList: ")
	whereClause = str(raw_input( "whereClause: "))
	if ( whereClause != None or whereClause != '' ): 
		whereClause += "WHERE "+ whereClause
	print db2_info.execSql4Str( conn, db2_info.getSqlByCols('cat.tables', columnList) )

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
