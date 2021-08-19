A line notify chat bot for birthday project
```
from datetime import datetime
import csv
import time
import requests
import urllib.parse
import sys

while(True):
	with open('vocab.csv','r') as csv_file:
		csv_reader = csv.reader(csv_file)
		dt = datetime.now().strftime('%Y%m%d%H%M')
		dtime = int(dt)
		
		for line in csv_reader:
			if int(line[1]) == dtime:
				
				url = 'https://notify-api.line.me/api/notify'

				# พี่บอย
				# token = 'LmVMc9pPaLI4KZ5xlhBDJUPFIFD6ng2a7hjQsDZfiRi'
			
				# กลุ่มงาน ปตท. 
				token = 'deH3gYBSmFskiJAhi3NxVv3hhfvzXArVlRDGxkCbItn'
			
				# Instrument Test
				team_token = 'G4U2fJZ8y3RCJ8cRqkaft5WsIn7x3bFMXM3Hj6CLkvR'

				#headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
				headers = {"Authorization":"Bearer "+token}
				team_headers = {"Authorization":"Bearer "+team_token}
				# msg = 'วันที่',datetime.now().strftime('%d/%m/%Y'),'วันนี้',line[0]
				#msg = ({ 'message':"line[0]",'imageFullsize':'pim1.jpg'})
				#img_path = '/home/serveradmin/Line/pim1.jpg'
				#file = {'imageFile':open('/home/serveradmin/Line/pim1.jpg','rb')}
				file = {'imageFile':open('./pim1.jpg','rb')}
				msg = line[0]

				session = requests.Session()
				#r = session.post(url, headers=headers , files=file, data = {'message':msg})
				r = session.post(url, headers=headers , data = {'message':msg})
				team_r = session.post(url, headers=team_headers , data = {'message':msg})

				#r = requests.post(url, headers=headers , data = msg)
				# print(msg)
				# print('วันที่',datetime.now().strftime('%d/%m/%Y'),'วันนี้',line[0])
				#print(line[0])
				print(r.text)
				print(team_r.text)
				time.sleep(61) 

```