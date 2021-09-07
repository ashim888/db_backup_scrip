# A Backup Scrip For Database
--------------
It's a lazy scrip for backing up mysql databases from one server to another with ssh access

Motivation
--------------
Nothing much. Easy implementation. Hassle free work. Chill


Installation
--------------
To install backup-mysql
```
 $ pip install backup-mysql
```

Usage
--------------
A list of server details in the following format
```
clients=[{
    "client1":{
        "client":"client1",
        "mysql_user":"noroot",
        "mysql_pass":"norootp",
        "mysql_db":"db_client1",
        "mysql_host":"Myysql_Host_IP",
        "sender_email":"backup@email.com",
        "sender_pass":"sender_password",
        "receiver_email":"receiver@email.com",
        "smtp_ssl_host":"mail.fintechnepal.com",
        "smtp_ssl_port":465,
        "backup_server_user":"server_username",
        "backup_server_ip":"backup_server_ip",
        "backup_server_port":"port_number_if_not_22"
    },
    "client2":{
        "client":"Client_name",
        "mysql_user":.....
    }
}]


```

Implementation
--------------
we can pass above dictionary to the BackupMysql Class as following:
```
obj=BackupMysql(clients)
```
After an object has been created with values of our databases and server

-  `obj.get_db_backup()` : This will create a database backup, zips it and pushes it to the backup server  
-  `obj.email_send()` : This will send email to the client's email address with backup as a zipped equipment
-  `obj.rm_db_backup()` : After Above two process this function will delete the backup and zipped file from the local machine
