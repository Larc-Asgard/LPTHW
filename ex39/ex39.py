states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',#CALEXIT
    'New York': 'NY',#concrete jungle where dreams are made
    'Michigan': 'MI'
}

cities = {
    'CA': 'Los Angeles',#Hollywood baby
    'MI': 'Detroit',#Eminem
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'#just bought a pair of Danner shoes from Portland

print '-' * 10
print 'NY State has: ', cities['NY']
print 'OR State has: ', cities['OR']

print '-' * 10
print 'Short for Michigan is: ', states['Michigan']
print 'Short for Florida is: ', states['Florida']

print '-' * 10
for state, abbrev in states.items():
    print '%s is called %s in short'% (state, abbrev)

print '-' * 10
for state, city in states.items():
    print '%s has the city %s'% (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print '%s is called %s in short and the city %s'% (state, abbrev, cities[abbrev])
    #just the #(being longer here)

print '-' * 10
state = states.get('Texas')

if not state:
    print 'Sorry, no Trump supporters'

city = cities.get('TX', "Error 404")#Two items, a key and a value
print "The city for the state 'TX' is %s" % city
