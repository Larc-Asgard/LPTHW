def add(a,b):
  print "ADDING %d + %d" %(a, b)
  return a +b

def subtract(a ,b):
  print "SUBTRACTUNG %d - %d" % (a, b)
  return a - b

def multiply(a,b):
  print "MULTIPLYING %d + %d" %(a, b)
  return a * b

def divide(a,b):
  print "DIVIDING %d + %d" %(a, b)
  return a / b

print "Doing math with only functions now"

age = add(20,3)
height = subtract (180, 2)
weight = multiply (30, 2)
iq = divide (240, 2)

print "Age: %d, Height %d, Weight %d, IQ %d" %(age, height, weight, iq)

# Extra Puzzle

print "Please figure out the formula, which is composed of the previously given number, in order to give the following number:"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print what
