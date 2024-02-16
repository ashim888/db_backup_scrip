#!/bin/bash

CURRENTDATE=`date +"%Y-%m-%d"`

#DUMP AND SAVE
mysqldump -u $1 --password=$2 $3 > $HOME/db_backup/$4_db_${CURRENTDATE}.sql

#GZIP DB
zip $HOME/db_backup/$4_db_${CURRENTDATE}.zip $HOME/db_backup/$4_db_${CURRENTDATE}.sql

# SCP TO BACKUP SERVER
scp -P $7 $HOME/db_backup/$4_db_${CURRENTDATE}.zip $5@$6:/home/deploy/db_backup

