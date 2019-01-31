#!/usr/bin/env python

input_file=open('data_marta.txt', 'rU')

answer = 0
for line in input_file:
	if line != "":
		print str(answer) + " "+ "+"+ str(line)
		answer = answer + int(line)
print answer
