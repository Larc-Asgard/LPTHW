# -*- coding utf-8 -*-
from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "Print the whole file:\n"
print_all(current_file)

print "Rewind:\n"
rewind(current_file)
#so it has some sort of pointer to read a file making a rewind necessary here?
print"Print three lines:\n"
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line, current_file)
