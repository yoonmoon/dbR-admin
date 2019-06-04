from db2 import event_mon
from db2 import db2_info
import ibm_db
import sys
import os
from common import shell_ext
from common import config
import readline

config.saveSecret()

print config.getSecret()

os.environ['DBR_MODULE']='testing module'
os.environ['DBR_ACTION']='testing action'
print(os.environ['DBR_MODULE'])
print(os.environ['DBR_ACTION'])

print('Enter Your Action:')
DBR_ACTION = input()

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
