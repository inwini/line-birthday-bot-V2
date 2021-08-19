from datetime import datetime
import csv
import time
import requests
import urllib.parse
import sys

while(True):
	with open('vocab.csv','r', encoding="utf8") as csv_file:
		csv_reader = csv.reader(csv_file)
		dt = datetime.now().strftime('%m%d%H%M')
		dtime = int(dt)
		
		for line in csv_reader:
			if int(line[1]) == dtime:
				
				url = 'https://notify-api.line.me/api/notify'

				# Test
				# token = 'WpfUF1MRcrgnfD5vmk9wFuBscToUiPDgxEYu4MJ4Bn4'
			
				# กลุ่มงาน ปตท. 
				token = 'deH3gYBSmFskiJAhi3NxVv3hhfvzXArVlRDGxkCbItn'

				headers = {"Authorization":"Bearer "+token}
				# team_headers = {"Authorization":"Bearer "+team_token}
				
				file = {'imageFile':open('./pim1.jpg','rb')}
				msg = line[0]

				session = requests.Session()
				# r = session.post(url, headers=headers , data = {'message':msg})
				r = session.post(url, headers=headers , files=file, data = {'message':msg})
				# team_r = session.post(url, headers=team_headers , data = {'message':msg})
			
				# print(r.text)
				
				time.sleep(61) 
