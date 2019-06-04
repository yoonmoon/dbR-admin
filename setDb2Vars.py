from db2 import db2_info
import os
from common import shell_ext
from common import config
import readline

def settingInput( envName, list ):
	shell_ext.setInputList( db2_info.getDatabaseList() )
	default = os.getenv(envName)
	print " +default=", default
	newVal = raw_input(envName+ " [%s]: " % default)
	newVal = newVal or default
	print " setting ", envName, "=", newVal
	os.environ[envName] = newVal

settingInput( 'dbR_database', db2_info.getDatabaseList() )
settingInput( 'dbR_user', [] )
config.saveSecret()
#settingInput( 'dbR_password', [] )



