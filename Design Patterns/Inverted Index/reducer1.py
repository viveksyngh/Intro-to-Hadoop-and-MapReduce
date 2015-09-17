#!/usr/bin/python
import sys
oldWord = None
indexes = []
count = 0
for line in sys.stdin :
	data = line.strip().split("\t")
	if len(data) != 2 :
		continue
	curWord , curIndex = data
	if 'fantastic' in curWord :
		if 'fantastically' not in curWord :
			count += 1
	if 'fantastically' in curWord :
		indexes.append(curIndex)
		indexes.sort()
print "{0}\t{1}".format(count, indexes)


