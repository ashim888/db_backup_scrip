#!/usr/bin/python

import smtplib
import base64
from datetime import datetime

now=datetime.now()
date_format="%Y-%m-%d"
time1=now.strftime(date_format)

# print(time1)

filename="/home/fintech/db_backup/jmc_db_{}.zip".format(time1)
print(filename)

#filename = "/tmp/test.txt"
# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

'''
EMAIL DETAILS
'''
sender = 'backup@fintechnepal.com'
account_password = 'dUEg{u5OfVOQ'
receiver = 'paudelbhisma@gmail.com'
#receiver = 'rabim55@gmail.com'

marker = "AUNIQUEMARKER"

body ="""
This is a data backup email of the system.
"""
# Define the main headers.
part1 = """From: JMC Database Backup <backup@fintechnepal.com>
To: JMC <paudelbhisma@gmail.com>
Subject: DATABASE BACKUP for %s
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (time1, marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
    smtp_server = smtplib.SMTP_SSL("mail.fintechnepal.com", 465)
    smtp_server.login(sender, account_password)
    smtp_server.sendmail(sender, receiver, message)
    smtp_server.close()
except Exception as exc:
    print(exc)
