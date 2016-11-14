things = "Apples Oranges Lemons Bananas Pears Grapes"

print "Error. There are not 10 things in the list. Pending for fix..."

stuff = things.split(" ")
more_stuff = ["Days", "Night", "Dawn", "Dusk", "Morning", "Noon", "Afternoon", "Evening"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now."% len(stuff)
#I've just realized comment is part of the grade
#so here len() extracts the length of the given list stated inisde the ()
#append would add the required item into a list while expanding it

print "Listing: ", stuff
print "Let's do some things with them."

print stuff[1]
#second items
print stuff[-1]
#since it is counting the space, so 10 spaces counted would mean 11 items
#here it gets the last item on the list
print stuff.pop()
print " ".join(stuff)
#joining everything on the list with a space in between
print "#".join(stuff[3:5])
#joining the third and fifth item with # in between
