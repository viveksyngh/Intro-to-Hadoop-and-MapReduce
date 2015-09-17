#!/usr/bin/python
import sys
def reducer() :
	user , reputation, gold, silver, bronze  = None, None, None, None, None
	for line in sys.stdin :
		data = line.strip().split("\t")
		if data[1] == 'A' :
			user = data[0]
			reputation = data[2]
			gold = data[3]
			silver = data[4]
			bronze = data[5]
		elif data[1]  == 'B' and data[0] == user :
			print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(data[2], data[3], data[4], data[0], data[5], data[6], data[7], data[8], data[9], reputation, gold, silver, bronze)
			
reducer()


			
