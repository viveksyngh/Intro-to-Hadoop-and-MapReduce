#!/usr/bin/python
import sys
hits = 0
oldHost = None
for line in sys.stdin :
	data = line.split('\t')
	if len(data) != 2 :
		continue
	curHost, page = data
	if oldHost and oldHost != curHost :
		print "{0}\t{1}".format(oldHost, hits)
		hits = 0
		oldHost = curHost
	oldHost = curHost
	hits += 1
if oldHost != None :
	print "{0}\t{1}".format(oldHost, hits)
 
