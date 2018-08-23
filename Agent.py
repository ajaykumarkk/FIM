import os, sys,uuid
import hashlib
from multiprocessing import Process,Manager
import json
import time
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import urllib.request
from email.utils import COMMASPACE, formatdate
from email import encoders


def dir_list(path):#this function parses through the directories until a file is found
	global files
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
				files.append(abs_path)
					

def hash_cal(start,end,fl,hash):#this function calculates the hash value
	#print(".")
	for i in range(start,end+1):
		#print(str(fl[i])+"<--"+str(i))
		inputFile=fl[i]
		with open( inputFile , "rb" ) as openedFile:
			#print(openedFile)
			while True:
				readFile = openedFile.read(2**20)
				if not readFile:
					break;
				md5Hash = hashlib.md5(readFile)
				md5Hashed = md5Hash.hexdigest()
				hash[inputFile]=md5Hashed
	
	
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
	return

def diff(dcalculated,dformfile,ddiff):
	if dcalculated == dformfile:
			pass
	else:
			for key in dcalculated.keys():
				if key not in dformfile.keys():
					#print(key)
					ddiff[key]=dcalculated[key]
				else:
					if dformfile[key] != dcalculated[key]:
						#print(key)
						ddiff[key]=dformfile[key]+'#'+dcalculated[key]
	return 
	
if __name__ == '__main__':
	ddiff={}
	manager = Manager()
	URL = "http://192.168.51.53/fim/php/getSysId.php"
	x=(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
	for ele in range(0,8*6,8)][::-1]))
	PARAMS = {'mac_id':x}
	r = requests.get(url = URL, params = PARAMS)
	sysID = r.text
	d2={}
	files=manager.list()
	hash=manager.dict()																#C:/Users/ajayk/OneDrive/Documents/IIDT/Assignments/Forensics
	dir_list(sys.argv[1])
	if len(files) <5:
		#hash_cal(0,len(files),files,hash)
		p = Process(target=hash_cal, args=(0,len(files)-1,files,hash))
		p.start()
		p.join()
		if os.path.isfile('hashfile.txt'):
			d2 = json.load(open("hashfile.txt"))		
	else:
		process=[]
		e1=len(files)//5
		#print(e1)
		p1 = Process(target=hash_cal, args=(0,e1,files,hash))
		p1.start()
		process.append(p1)
		p2 = Process(target=hash_cal, args=(e1+1,2*e1+1,files,hash))
		p2.start()
		process.append(p2)
		s3=2*e1+2
		p3 = Process(target=hash_cal, args=(s3,e1+s3,files,hash))
		p3.start()
		process.append(p3)
		s4=e1+s3+1
		p4 = Process(target=hash_cal, args=(s4,s4+e1,files,hash))
		p4.start()
		process.append(p4)
		s5=s4+e1+1
		p5 = Process(target=hash_cal, args=(s5,len(files)-1,files,hash))
		p5.start()
		process.append(p5)
		for p in process:
			p.join()
		if os.path.isfile('hashfile.txt'):
			d2 = json.load(open("hashfile.txt"))
		while len(process) > 0:
			process = [job for job in process if job.is_alive()]
			print(".")
			time.sleep(1)
		
		for p in process:
			p.wait()
	
	json.dump(hash.copy(), open("hashfile.txt",'w'))
	diff(hash,d2,ddiff)
	print(ddiff)
	print("Sending the POST to the server")
	if len(ddiff.keys()) > 0:
		PARAMS = json.dumps(ddiff)
		URL = "http://192.168.51.53/fim/php/loadHash.php"
		da = {'hashes':PARAMS,'sysid':sysID}
		r1 = requests.post(url = URL, data = da)
		print(r1.text);
		body = "Results from the system "+x+"  "
		for key in ddiff.keys():
			body=body+key
		sendmail(body)
	
	