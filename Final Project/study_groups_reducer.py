#!/usr/bin/python
import sys
prev_node = None
students = [] 
for line in sys.stdin :
	data = line.strip().split()
	cur_node, student = data
	if prev_node and prev_node != cur_node :
		print "{0}\t{1}".format(prev_node, students)
		students = []
	prev_node = cur_node
	students.append(int(student))
if prev_node != None :
	print "{0}\t{1}".format(prev_node, students)

