#!/usr/bin/python

import smtplib
import base64
from datetime import datetime
import os,subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class SendBackupEmail:
    def __init__(self,args):
        # self.client, self.mysql_usr,self.mysql_pass,self.mysql_db = dict(args)
        # self.args=dict(args)
        self.client = args.get('client')
        self.mysql_user=args.get('mysql_user')
        self.mysql_pass=args.get('mysql_pass')
        self.mysql_db=args.get('mysql_db')
        self.mysql_host=args.get('mysql_host')
        self.now=datetime.now()
        self.date_format="%Y-%m-%d"
        self.time1=self.now.strftime(self.date_format)
        self.db_path=os.getcwd()
        self.sender="backup@fintechnepal.com"
        self.sender_pass=args.get('sender_pass')
        self.receiver=args.get('receiver_email')
        self.smtp_ssl_host = "mail.fintechnepal.com"  # smtp.mail.yahoo.com
        self.smtp_ssl_port = 465


    def get_db_backup(self):
        # self.dumpcmd = "mysqldump -h " + self.mysql_host + " -u " + self.mysql_user + " -p " + self.mysql_db + " > " + self.db_path + "/" +self.client+"_" +self.time1+ ".sql"
        # print(self.dumpcmd)
        # os.system(dumpcmd)
        subprocess.call(["/Users/ashim888/Documents/db_config/script.sh",self.mysql_user,self.mysql_pass,self.mysql_db,self.client])
        print("db backup complete")

    def email_send(self):
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        import smtplib
        import mimetypes
        import email.mime.application

        s = smtplib.SMTP_SSL(self.smtp_ssl_host, self.smtp_ssl_port)
        s.login(self.sender, self.sender_pass)

        self.msg = MIMEMultipart()
        self.msg['Subject'] = '{} Backup for {}'.format(self.client,self.now)
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        self.txt = MIMEText('Database Backup')
        self.msg.attach(self.txt)

        # filename = 'introduction-to-algorithms-3rd-edition-sep-2010.pdf' #path to file
        self.filename = "{}/db_backup/{}_db_{}.zip".format(os.getcwd(),self.client,self.time1)
        print(self.filename)
        fo=open(self.filename,'rb')
        attach = email.mime.application.MIMEApplication(fo.read(),_subtype="zip")
        fo.close()
        attach.add_header('Content-Disposition','attachment',filename=self.filename)
        self.msg.attach(attach)
        s.send_message(self.msg)
        s.quit()

values={"client":"ABC Corp",
        "mysql_user":"root",
        "mysql_pass":"Anonymous@123!@#",
        "mysql_db":"studysys",
        "mysql_host":"localhost",
        "sender_pass":"dUEg{u5OfVOQ",
        "receiver_email":"ashim.lamichhane@fintechnepal.com"}
obj=SendBackupEmail(values)
obj.get_db_backup()
obj.email_send()