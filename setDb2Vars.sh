#/bin/sh

read -p 'Action: ' dbR_action
read -p 'Database: ' dbR_database 
read -p 'User: ' dbR_user
read -sp 'Password: ' dbR_password
read -p 'Schema: ' dbR_schema
echo $dbR_database
echo $dbR_user
export dbR_action=$dbR_action
export dbR_database=$dbR_database
export dbR_user=$dbR_user
export dbR_password=$dbR_password
export dbR_schema=$dbR_schema
