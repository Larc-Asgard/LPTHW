# Here's how you define the blueprint for your new Bookcase objects
class Bookcase(object):
    def __init__(self, w, h):
        print "Making a new bookcase..."
        self.width = w
        self.height = h

    def __str__(self):
        return self.prettyprint()

    def prettyprint(self):
        return "A generic bookcase"

class Billy(Bookcase):
    def __init__(self, width, height):
        super(Billy, self). __init__(width, height)
        self.color = "red"

    def prettyprint(self):
        pretty = "A Billy Bookcase with dimensions %d x %d cm"
        return pretty % (self.width, self.height)

class Hemnes(Bookcase):
    def __init__(self, width, height):
        super(Hemnes, self). __init__(width, height)
        self.color = "red"

    def prettyprint(self):
        pretty = "A Hemnes Bookcase with dimensions %d x %d cm"
        return pretty % (self.width, self.height)

gen = Bookcase(50, 100)
bil = Billy(80, 120)
hem = Hemnes(200,100)

print hem.prettyprint()

print "Type: \n%r\n%r\n%r"% (type(gen), type(bil), type(hem))
print "Raw: \n%r\n%r\n%r"% (gen ,bil, hem)
print "Pretty: \n%s\n%s\n%s"% (gen ,bil, hem)

print "Is instance of Billy?", isinstance (gen, Billy)
print "Is instance of Billy?", isinstance (bil, Billy)
print "Is instance of Billy?", isinstance (hem, Billy)
