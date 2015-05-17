#!/usr/bin/python
import sys
hits = 0
oldPage = None
maxHit = 0
popularPage = None
for line in sys.stdin :
	data = line.split('\t')
	if len(data) != 2 :
		continue
	curPage, ip = data
	if oldPage and oldPage != curPage :
		if maxHit < hits :
			maxHit = hits
			popularPage = oldPage
		hits = 0
		oldPage = curPage
	oldPage = curPage
	hits += 1
if oldPage != None :
	if maxHit < hits :
		maxHit = hits
		popularPage = oldPage
print "{0}\t{1}".format(popularPage, maxHit)
 
