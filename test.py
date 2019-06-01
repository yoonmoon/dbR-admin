from db2 import event_mon
import ibm_db
import sys

database=sys.argv[1]
user=sys.argv[2]
password=sys.argv[3]
try:
	action=sys.argv[4]
except Exception as e:
	action='listEM'

conn = ibm_db.connect(database, user, password)

if action == 'listEM':
	event_mon.listEventMon( conn )

if action == 'enable':
	event_mon.enableDefaultClass( conn )

if action == 'creatEM':
	event_mon.createEventMon( conn, 'TEST1', '', '' )

if action == 'selectEM':
	print action
	event_mon.selectEventMon( conn, 'CONN_DB_APPLS', '', '' )

if action == 'dropEM':
	print action
	event_mon.dropEventMon( conn, 'CONN_DB_APPLS', '', '' )

ibm_db.close(conn)
