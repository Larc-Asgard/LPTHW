# -*- coding: utf-8 -*-

cars = 100
space = 4.0
drivers =30
passengers = 90
car_unused = cars - drivers
car_used = drivers
carpool = car_used * space
average_passengers = passengers / car_used

print "Numbers of cars:", cars
print "Numbers of drivers:", drivers
print "Numbers of Empty cars", car_unused
print carpool, "people will be transported"
print "Numbers of passengers:", passengers
print "On average, there are", average_passengers, " people in a car"
