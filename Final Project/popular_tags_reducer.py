#!/usr/bin/python
import sys
from operator import itemgetter
top_tags = []
old_tag = None
count = 0
for line in sys.stdin :
	data = line.strip().split()
	cur_tag = data[0]
	if old_tag and old_tag != cur_tag :
		if len(top_tags) < 10 :
			top_tags.append((old_tag, count))
		elif len(top_tags) == 10 :
			if top_tags[9][1] < count :
				top_tags.pop()
				top_tags.append((old_tag, count))
		top_tags.sort(key = itemgetter(1), reverse = True)
		count = 0
	old_tag = cur_tag
	count += 1
if old_tag != None :
	if len(top_tags) < 10 :
 		top_tags.append((old_tag, count))
        elif len(top_tags) == 10 :
		if top_tags[9][1] < count :
                	top_tags.pop()
                	top_tags.append((old_tag, count))
        top_tags.sort(key = itemgetter(1), reverse = True)
for tag in top_tags :
	print "{0}\t{1}".format(tag[0], tag[1])


		
			
