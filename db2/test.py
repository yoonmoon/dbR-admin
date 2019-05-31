import ibm_db
import string
import os
import time
import sys

database=sys.argv[1]
user=sys.argv[2]
password=sys.argv[3]
conn = ibm_db.connect(database, user, password)
print conn
