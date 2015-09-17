#!/usr/bin/python
import sys 
for line in sys.stdin :
	data = line.split(' ')
	if len(data) == 10:
		ip = data[0]
		page = data[6]
		page = page.replace("http://www.the-associates.co.uk",'')
		print '{0}\t{1}'.format(page, ip)	

