#!/usr/bin/python
'''
Multiple DB with multiple creds
'''
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
        "mysql_user":"mysql_user",
        "mysql_pass":"mysql_pass",
        "mysql_db":"db_name",
        "mysql_host":"localhost",
        "sender_email":"sender_email",
        "sender_pass":"sender_email_password",
        "receiver_email":"hhane@email.com",
        "smtp_ssl_host":"mail.email.com",
        "smtp_ssl_port":465,
        "backup_server_user":"username",
        "backup_server_ip":"",
        "backup_server_port":""
    }
}]


