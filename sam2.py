#!/usr/bin/python
path_list=[] 
import os, sys,uuid
import hashlib
import requests
import json
import uuid
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import urllib.request
from email.utils import COMMASPACE, formatdate
from email import encoders
import time
y=[]
dcalculated={}
dformfile={}
ddiff={}
def hash_cal(filename):#this function calculates the hash value
    ###inputFile = input("Enter the name of the file:")
    inputFile=filename
    openedFile = open(inputFile,'rb')
    readFile = openedFile.read()
    md5Hash = hashlib.md5(readFile)
    md5Hashed = md5Hash.hexdigest()
    a1=md5Hashed
    a2=inputFile
    global y
    global dcalculated
    y = [a2,a1]
    dcalculated[a2]=a1
    #print (y)
    with open("outfile.txt","a") as fp:
        fp.write("  %s" % y+"\n") #create a new file with read only permissions
	
    

        
def sendmail(alert):
   fromaddr = ''
   toaddrs = ''

   msg = MIMEMultipart()
   msg['Date'] = formatdate(localtime=True)
   msg = MIMEMultipart('alternative')
   msg['Subject'] = "hashvalue"
   msg['From'] = fromaddr #like name
   msg['To'] = toaddrs

   body = MIMEText(str(alert))
   msg.attach(body)

   username = ''
   password = ''
   server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
   server.login(username, password)
   server.sendmail(fromaddr, toaddrs, msg.as_string())
   server.quit()
   return 
   
def dir_list(path):#this function parses through the directories until a file is found
    dirs = os.listdir( path )
    for file in dirs:
        abs_path = path+'//'+file
        if os.path.isdir(abs_path):
            dir_list(abs_path)
        else:
            path_list.append(abs_path)
            hash_cal(abs_path)
        
def readHash():#collects the path and has value of each file keeps ina text document and delets it after use
    with open("outfile.txt","r") as ff:
        lines=ff.readlines()
        for line in lines:
            l=len(line)
            x=line[:-3].rfind("'")
            s=line[x+1:-3]
            f=line[4:].find("'")
            r=line[4:f+4]
            global dformfile
            dformfile[r]=s
            #read path and store in dictornary delete filoe at the end of this func
            ff.close()
        os.remove("outfile.txt")
        

def diff():#checks the diifrence hash value changed fle and returns the path
    if dcalculated == dformfile:
        pass
        #print("yes")
        #print(dcalculated) the path and the hash values are matched 
    else:
        ##print("sorry")
        global ddiff
        for key in dcalculated.keys():
            if key not in dformfile.keys():
                #print(key)
                ddiff[key]=dcalculated[key]
            else:
                if dformfile[key] != dcalculated[key]:
                    #print(key)
                    ddiff[key]=dformfile[key]+'#'+dcalculated[key]
    return        
        

		
if os.path.isfile('outfile.txt'):
    readHash()
dir_list("F:/")

diff()
print(ddiff)
if len(ddiff.keys()) > 0:
	for key in ddiff.keys():
		body=body+key
	sendmail(body)