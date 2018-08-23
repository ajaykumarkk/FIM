import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import urllib.request
from email.utils import COMMASPACE, formatdate
from email import encoders
import hashlib
import time
import sys

def sendmail(alert):
   fromaddr = 'fortestingcodes@gmail.com'
   toaddrs = 'ajaykumarkk77@gmail.com'

   msg = MIMEMultipart()
   msg['Date'] = formatdate(localtime=True)
   msg = MIMEMultipart('alternative')
   msg['Subject'] = "hashvalue"
   msg['From'] = fromaddr #like name
   msg['To'] = toaddrs

   body = MIMEText(str(alert))
   msg.attach(body)

   username = 'fortestingcodes@gmail.com'
   password = 'srinuiidt25'
   server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
   server.login(username, password)
   server.sendmail(fromaddr, toaddrs, msg.as_string())
   server.quit()
   

