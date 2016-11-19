#override the parent behaviour with desired child behaviour input


class Parent(object):
    def override(self):
        print "PARENT override()"

class Child(Parent):
    def override(self):
        print "CHILD override()"
dad = Parent()
son = Child()

dad.override()
son.override()
