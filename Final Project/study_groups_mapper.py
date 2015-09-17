#!/usr/bin/python
import sys
import csv
reader = csv.reader(sys.stdin, delimiter="\t")
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
for line in reader :
	if line[5] == 'question' :
		print "{0}\t{1}".format(line[0],line[3])
	elif line[5] == 'answer' or line[5] == 'comment' :
		print "{0}\t{1}".format(line[6], line[3])

