#!/usr/bin/python
import sys
oldWord = None
indexes = []
count = 0
for line in sys.stdin :
	data = line.split("\t")
	if len(data) != 2 :
		continue
	curWord = data[0]
	curIndex = data[1].strip("\n")
	if curIndex == '' or curIndex == 'id' :
		continue
	if oldWord and oldWord != curWord :
		print "{0}\t{1}\t{2}".format(oldWord,indexes, len(indexes))
		indexes = []
		oldWord = curWord
	oldWord = curWord
	indexes.append(int(curIndex))
if oldWord != None :
	print "{0}\t{1}\t{2}".format(oldWord, indexes,len(indexes))

