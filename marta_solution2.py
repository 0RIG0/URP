#!/usr/bin/python

myfile = open("data_marta.txt", "rU")
lines = myfile.readlines() # I am reading lines here
total = 0 #total update each time number is entered

for line in lines:   #takes each line in the loop
	conv_int = int(line) # convert is from string to int
	total =total + conv_int #updates the counter 
	 
print total #prints my total sum


 
