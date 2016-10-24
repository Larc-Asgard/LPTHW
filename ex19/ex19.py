# -*- coding utf-8 -*-
#def a function to do certain thing.
def milk_and_oreo (milk_count, oreo_count):
    print "You have %d bottles of milks" % milk_count
    print "And you have %d Oreo." % oreo_count
    print "Lecker.\n"

print "Directly assign numbers to the function by milk_and_oreo(20,30)"
milk_and_oreo(20,30)

print "Or define the variables in the script:"
milk_count2 = 10
oreo_count2 = 50
milk_and_oreo(milk_count2, oreo_count2)

print "Calculation is also supported!"
milk_and_oreo(milk_count2+1, oreo_count2+2)
