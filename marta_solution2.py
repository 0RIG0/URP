#!/usr/bin/python

myfile = open("data_marta.txt", "rU")
lines = myfile.readlines()
total = 0 #total update each time number is entered

for line in lines:
	conv_int = int(line)
	total =total + conv_int
	 
print total 

print ("total is ")
 
