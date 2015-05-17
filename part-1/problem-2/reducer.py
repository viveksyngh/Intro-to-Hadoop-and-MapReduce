#!/usr/bin/python
import sys
sales = 0.0
oldItem = None
for line in sys.stdin :
	data = line.strip().split("\t")
	if len(data) != 2 :
		continue
	curItem, curValue = data
	if oldItem and curItem != oldItem :
		print "{0}\t{1}".format(oldItem, sales)
		oldItem = curItem
		sales = 0.0
	oldItem = curItem 
	if sales < float(curValue) :
		sales = float(curValue)
if oldItem != None :
	print "{0}\t{1}".format(oldItem, sales)


