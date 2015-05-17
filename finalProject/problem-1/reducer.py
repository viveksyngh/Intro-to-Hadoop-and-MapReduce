#!/usr/bin/python
import sys
hits = 0
oldPage = None
for line in sys.stdin :
	data = line.split('\t')
	if len(data) != 2 :
		continue
	curPage, ip = data
	if oldPage and oldPage != curPage :
		print "{0}\t{1}".format(oldPage, hits)
		hits = 0
		oldPage = curPage
	oldPage = curPage
	hits += 1
if oldPage != None :
	print "{0}\t{1}".format(oldPage, hits)
 
