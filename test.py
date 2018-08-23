#!/usr/bin/python
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
hash={}

def hash_cal(filename):#this function calculates the hash value
	###inputFile = input("Enter the name of the file:")
	global hash
	inputFile=filename
	with open( inputFile , "rb" ) as openedFile:
		print(openedFile)
		while True:
			readFile = openedFile.read(2**20)
			if not readFile:
				break;
			md5Hash = hashlib.md5(readFile)
			md5Hashed = md5Hash.hexdigest()
			hash[inputFile]=md5Hashed
	




def dir_list(path):#this function parses through the directories until a file is found
	try:
		dirs = os.listdir( path )
	except:
		return
	for file in dirs:
		if not file.startswith('.'):
			abs_path = path+'//'+file
			if os.path.isdir(abs_path):
				dir_list(abs_path)
			else:
				try:
					hash_cal(abs_path)
				except:
					pass


      



dir_list("F:/setups")
print(len(hash))

