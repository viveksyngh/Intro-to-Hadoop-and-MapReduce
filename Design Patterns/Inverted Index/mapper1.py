#!/usr/bin/python
import csv
import sys
import re
reader = csv.reader(sys.stdin, delimiter="\t")
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
for line in reader :
	id = line[0]
	line[4] = line[4].lower()
	words = re.split(r'[-.,?!:;/"()<>#$=[\]" "\t\n]', line[4])
	for word in words :
		if len(word) == 0 :
			continue
		if 'fantastic' in word :
			print "{0}\t{1}".format(word, id)



	
