#!/usr/bin/python
import sys
totalSales = 0.0
salesCount = 0
for line in sys.stdin :
	data = line.strip().split("\t")
	if len(data) != 2 :
		continue
	curItem, curValue = data
	salesCount += 1
	totalSales += float(curValue)
print "{0}\t{1}".format(totalSales, salesCount)


