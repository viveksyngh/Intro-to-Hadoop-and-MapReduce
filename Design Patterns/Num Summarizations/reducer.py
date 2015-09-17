#!/usr/bin/python
import sys
prevDay = None
Count = 0
Sales = 0.0
for line in sys.stdin :
	data = line.strip().split("\t")
	if len(data) != 2 :
		continue
	curDay, curSales = data 
	if prevDay and curDay != prevDay :
		print "{0}\t{1}".format(prevDay , Sales/Count)
		Count = 0
		Sales = 0.0
	prevDay = curDay
	Sales += float(curSales)
	Count += 1
if prevDay != None :
	print"{0}\t{1}".format(prevDay, Sales/Count)
 
