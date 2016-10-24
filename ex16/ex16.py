# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv

print "%r is about to be erased." % filename
print "If you wish to cancel this action, please press CTRL-C (^C)."
print "It you wish to proceed, please press Enter."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file..."
target.truncate()

print "Please now enter three lines:"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "It will be written into the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Closing..."
target.close()
