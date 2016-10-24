# -*- coding: utf-8 -*-

name = "Leica Nocticron 42.5 f/1.2"
focal_length = 42.5
aperature = 1.2
crop_factor = 2
color = "black"
letter_color = "orange"

print "Let's talk about one of my favourite lens, %s"% name
print "It's focal length is %d"% focal_length
print "And it's aperature is f/%d"% aperature
print "The lens body is %s but it has the Leica signature %s letter."% (color, letter_color)

print "It is a %d, but with a crop factor of %d, it is actually a %d lens"% (focal_length,
 crop_factor, focal_length*crop_factor)
