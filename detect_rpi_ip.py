#cmd /k netsh interface ip delete arpcache 

import os
import subprocess
import ConfigParser 

cfg = ConfigParser.ConfigParser()
currFolder = os.path.dirname(os.path.abspath( __file__ ))

if os.path.isfile(currFolder+"/config.ini"):
	cfg.read(currFolder+"/config.ini")
	
	for i in range(int(cfg.get('address', 'ipRangeMin')),int(cfg.get('address', 'ipRangeMax'))):
		os.system("ping "+cfg.get('address', 'ipPrefix')+"."+str(i)+" -n 1 -w 50")
	os.system("arp -a")

	arp = subprocess.check_output("arp -a ", shell=True)
	split = arp.split("\n")

	i = 0
	ip =""
	for line in split:
		if line.count(cfg.get('address', 'mac')):
			split2 = line.split(" ")
			for col in split2:
				if "192" in col:
					ip = col
			
		i += 1
	
	
	if ip is not "":
		print("Connecting to "+ip)
		os.system("\"C:\Program Files\putty\putty.exe\" -ssh "+cfg.get('auth', 'log')+"@"+ip+" -pw "+cfg.get('auth', 'pwd'))
	else:
		print("Error : ip not found")
else:
	print("Error : config.ini not found")

