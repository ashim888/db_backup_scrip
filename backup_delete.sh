#!/bin/bash

CURRENTDATE=`date +"%Y-%m-%d"`
# Remove From The Drive
rm -rf $HOME/db_backup/$1_db_${CURRENTDATE}.sql
rm -rf $HOME/db_backup/$1_db_${CURRENTDATE}.zip