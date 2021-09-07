#!/usr/bin/python

import smtplib
import base64
from datetime import datetime
import os,subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from client_details import values
from pathlib import Path

class SendBackupEmail:
    def __init__(self,args):
        self.client = args.get('client')
        self.mysql_user=args.get('mysql_user')
        self.mysql_pass=args.get('mysql_pass')
        self.mysql_db=args.get('mysql_db')
        self.mysql_host=args.get('mysql_host')
        self.backup_server_user=args.get('backup_server_user')
        self.backup_server_ip=args.get('backup_server_ip')
        self.backup_server_port=args.get('backup_server_port')
        self.now=datetime.now()
        self.date_format="%Y-%m-%d"
        self.time1=self.now.strftime(self.date_format)
        self.sender=args.get("sender_email")
        self.sender_pass=args.get('sender_pass')
        self.receiver=args.get('receiver_email')
        self.smtp_ssl_host = args.get('smtp_ssl_host')
        self.smtp_ssl_port = args.get('smtp_ssl_port')


    def get_db_backup(self):
        try:
            self.script_path=os.path.abspath(os.getcwd())+"/script.sh"
            subprocess.call([self.script_path,self.mysql_user,self.mysql_pass,self.mysql_db,self.client,self.backup_server_user,self.backup_server_ip,self.backup_server_port])
            print("DB backedup")
        except Exception as exc:
            print(exc)
    
    def rm_db_backup(self):
        try:
            self.script_path=os.path.abspath(os.getcwd())+"/backup_delete.sh"
            subprocess.call([self.script_path,self.client])
            print("DB deleted")
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
            print("Mail Sent")
        except Exception as exc:
            print(exc)

for x in values:
    for key,value in x.items():
        obj=SendBackupEmail(value)
        obj.get_db_backup()
        obj.email_send()
        obj.rm_db_backup()
        print("=====================")