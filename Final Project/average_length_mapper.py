#!/usr/bin/python
import sys
import csv
reader = csv.reader(sys.stdin, delimiter="\t")
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
for line in reader :
	if line[5] == 'question' :
		print "{0}\t{1}\t{2}".format(line[0], "A", len(line[4]))
	elif line[5] == 'answer' :
		print "{0}\t{1}\t{2}".format(line[6], "B", len(line[4]))
	else :
		continue


