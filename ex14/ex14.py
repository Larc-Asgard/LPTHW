# -*- coding: utf-8 -*-

from sys import argv

script, user_name = argv
prompt = "Input:"

print "HI %s, I'm the %s script:"%(user_name, script)
print "Here is a few questions for you, %s"% user_name

print "Please input your opinion toward Python or programming"
like = raw_input(prompt)

print "Please input your location"
live = raw_input(prompt)

print "Please state the device you are using"
computer = raw_input(prompt)

print """
Conclusion:
You said %r about Python, or programming.
You are using %r in %r
"""%(like, computer, live)
