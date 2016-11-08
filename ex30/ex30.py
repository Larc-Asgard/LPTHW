people = 30
cars = 40
trucks = 15

if cars > people:
    print "There are more cars than people."
elif cars < people:
    print "Too many people, not enough cars."
else:
    print "Unable to decide."

if trucks > cars:
    print "There are more trucks than cars."
elif trucks < cars:
    print "There are less trucks than cars."
else:
    print "Unable to decide."

if people > trucks:
    print "There are more people than trucks."
else:
    print "Or stay home?"
