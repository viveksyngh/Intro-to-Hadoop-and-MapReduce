#!/usr/bin/python
import sys
import csv
from datetime import datetime
reader = csv.reader(sys.stdin, delimiter="\t")
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
for line in reader :
	if line[8] == 'added_at':
		continue
	#date = datetime.replace(line[8],tzinfo=None)
	date = line[8][ :-3]
	date  = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
	hour = date.hour
	print "{0}\t{1}".format(line[3], hour)

