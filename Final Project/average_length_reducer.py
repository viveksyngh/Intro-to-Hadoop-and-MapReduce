#!/usr/bin/python
import sys
prev_id = None
ques_id = None 
count = 0
total_length = 0.0
for line in sys.stdin :
	data = line.strip().split('\t')
	id,type,length = data
	if prev_id and prev_id != id :
		if count == 0  :
			average = 0
		else :
			average = round((total_length/count), 2)
		print "{0}\t{1}\t{2}".format(prev_id, ques_length, average)
		total_length = 0
		count = 0
	prev_id = id 
	if type == "A" :
		ques_length = length 
	elif type == "B" :
		total_length += int(length)
		count += 1
if prev_id != None :
	if count == 0  :
		average = 0
	else :
		average = round((total_length/count), 2)

	print"{0}\t{1}\t{2}".format(prev_id, ques_length, average)
     
