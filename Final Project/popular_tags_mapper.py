#!/usr/bin/python
import sys
import csv
reader = csv.reader(sys.stdin, delimiter="\t")
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
for line in reader :
	if line[5] == "question" :
		tags = line[2].strip().split()
		for tag in tags :
			print "{0}\t{1}".format(tag, line[0])

