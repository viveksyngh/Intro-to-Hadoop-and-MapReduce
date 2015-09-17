#!/usr/bin/python
import sys
prev_id = None
max_hour = []
count = 0
MaxCount = 0
prev_hour = None
for line in sys.stdin :
	data = line.strip().split('\t')
	cur_id, hour = data
	if prev_id and cur_id != prev_id :
		if count > MaxCount :
                        max_hour = [prev_hour]
                elif count == MaxCount :
                        max_hour.append(prev_hour)
		MaxCount = count
                count = 0
		for h in max_hour :
			print "{0}\t{1}".format(prev_id, h)
		max_hour = []
		prev_hour = None
		MaxCount = 0
	prev_id = cur_id
	if prev_hour and prev_hour != hour :
		if count > MaxCount :
			max_hour = [prev_hour]
		elif count == MaxCount :
			max_hour.append(prev_hour)
		MaxCount = count
		count = 0
	prev_hour = hour
	if prev_id == cur_id and prev_hour == hour :
		count += 1

if prev_hour != None and count > MaxCount :
	max_hour.append(prev_hour)
if prev_id != None :
	for h in max_hour :
        	print "{0}\t{1}".format(prev_id, h)

	
