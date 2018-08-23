import os, sys,uuid
import hashlib
from multiprocessing import Process,Manager

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
	print(str(start)+"-->"+str(end))
	for i in range(start,end):
		print(str(fl[i])+"<--"+str(os.getpid() ))
		inputFile=fl[i]
		with open( inputFile , "rb" ) as openedFile:
			while True:
				readFile = openedFile.read(2**20)
				if not readFile:
					break;
				md5Hash = hashlib.md5(readFile)
				md5Hashed = md5Hash.hexdigest()
				hash[inputFile]=md5Hashed