from db2 import event_mon
from db2 import db2_info
import ibm_db
import sys
import os
from common import shell_ext
import readline

completer = shell_ext.Completer(db2_info.getDatabaseList())
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

print os.environ
default = shell_ext.getEnvironVar('PY_DATABASE')
print " +default=", default
database = raw_input("DATABASE [%s]: " % default)
database = database or default
print database

print(os.environ['PY_DATABASE'])
print(os.environ['PY_USER'])
print(os.environ['PY_PASSWORD'])
print(os.environ['PY_MODULE'])
print(os.environ['PY_ACTION'])

print('Enter Your Action:')
PY_ACTION = input()

try:
	action=sys.argv[4]
except Exception as e:
	action='listEM'

print "...", action
conn = ibm_db.connect(database, user, password)

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
