#/bin/sh

read -p 'Database: ' dbR_database 
read -p 'User: ' dbR_user
read -sp 'Password: ' dbR_password
echo $dbR_database
echo $dbR_user
export dbR_database=$dbR_database
export dbR_user=$dbR_user
export dbR_password=$dbR_password
