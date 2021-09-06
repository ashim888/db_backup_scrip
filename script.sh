#!/bin/bash

CURRENTDATE=`date +"%Y-%m-%d"`
#DB ACCESS
# username=root
# password=yarsha123!@#
# db_name=db_college_mgmt_updated


#DUMP AND SAVE
mysqldump -u $1 --password=$2 $3 > $HOME/Documents/db_config/db_backup/$4_db_${CURRENTDATE}.sql

#GZIP DB
zip $HOME/Documents/db_config/db_backup/$4_db_${CURRENTDATE}.zip $HOME/Documents/db_config/db_backup/$4_db_${CURRENTDATE}.sql
