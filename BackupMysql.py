#!/usr/bin/python

import time
from datetime import datetime
import os,subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from pathlib import Path
from client_details import clients
from dotenv import load_dotenv
load_dotenv()

class BackupMysql:
    def __init__(self,args):
        self.client = args.get('client')
        self.mysql_user=os.getenv("mysql_user")
        self.mysql_pass=os.getenv("mysql_pass")
        self.mysql_db=args.get('client')
        self.mysql_host=os.getenv("mysql_host")
        self.backup_server_user=os.getenv("backup_server_user")
        self.backup_server_ip=os.getenv("backup_server_ip")
        self.backup_server_port=os.getenv("backup_server_port")
        self.now=datetime.now()
        self.date_format="%Y-%m-%d"
        self.time1=self.now.strftime(self.date_format)
        self.sender= os.getenv("sender")
        self.sender_pass=os.getenv("sender_pass")
        self.receiver=os.getenv("receiver")
        self.smtp_ssl_host = os.getenv("smtp_ssl_host")
        self.smtp_ssl_port = os.getenv("smtp_ssl_port")


    def get_db_backup(self):
        try:
            self.script_path=os.path.abspath(os.getcwd())+"/script.sh"
            subprocess.call([self.script_path,self.mysql_user,self.mysql_pass,self.mysql_db,self.client,self.backup_server_user,self.backup_server_ip,self.backup_server_port])
            return True
        except Exception as exc:
            print(exc)
    

    def rm_db_backup(self):
        try:
            self.script_path=os.path.abspath(os.getcwd())+"/backup_delete.sh"
            subprocess.call([self.script_path,self.client])
            return True
        except Exception as exc:
            print(exc)


    def email_send(self):
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        import smtplib
        import email.mime.application
        try:
            s = smtplib.SMTP_SSL(self.smtp_ssl_host, self.smtp_ssl_port)
            s.login(self.sender, self.sender_pass)

            self.msg = MIMEMultipart()
            self.msg['Subject'] = '{} Backup for {}'.format(self.client,self.now)
            self.msg['From'] = self.sender
            self.msg['To'] = self.receiver

            self.txt = MIMEText('Database Backup')
            self.msg.attach(self.txt)

            self.filename = "{}/db_backup/{}_db_{}.zip".format(Path.home(),self.client,self.time1)
            print("File path for mail: ",self.filename)
            fo=open(self.filename,'rb')
            attach = email.mime.application.MIMEApplication(fo.read(),_subtype="zip")
            fo.close()
            attach.add_header('Content-Disposition','attachment',filename=self.filename)
            self.msg.attach(attach)
            s.send_message(self.msg)
            s.quit()
            print("MAIL SENT")
            return True
        except Exception as exc:
            print(exc)

# def trigger(values):
for x in clients:
    for key,value in x.items():
        # print(value)
        obj=BackupMysql(value)
        obj.get_db_backup()
        obj.email_send()
        time.sleep(10)
        obj.rm_db_backup()
    print(key," Backedup")

# class BizproBackup(BackupMysql):
#     # def __init__(self,args):
#     #     self.mysql_user=args.get('mysql_user')
#     #     self.mysql_pass=args.get('mysql_pass')
#     #     self.mysql_db=args.get('mysql_db')
#     #     self.mysql_host=args.get('mysql_host')
    
#     def get_access(self):
#         import pymysql.cursors
#         con = pymysql.connect(host=self.mysql_host,user=self.mysql_user,password=self.mysql_pass,database=self.mysql_db,cursorclass=pymysql.cursors.DictCursor)
#         with con.cursor() as cursor:
#             sql = "select * from fn_tenant_database"
#             cursor.execute(sql)
#             return cursor.fetchall()

#     def create_backup(self):
#         list_of_clients = self.get_access()
#         for x in list_of_clients:
#             # for data in x:
#             #     # print(data)
#             self.client = x["db_name"]
#             x["mysql_user"]=x["username"]
#             del x["username"]
#             x["mysql_pass"]= x["password"]
#             del x["password"]
#             x["mysql_db"]= x["db_name"]
#             del x["db_name"]
#             x["mysql_host"]=x["host"]
#             del x["host"]

#             self.get_db_backup()
#             self.email_send()
#         # self.rm_db_backup()

# BizproBackup({
#         "mysql_user":os.getenv("mysql_user"),
#         "mysql_pass":"Anonymous@123!@#",
#         "mysql_db":"db_bizpro_admin",
#         "mysql_host":"localhost",}).create_backup()