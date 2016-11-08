print "You are in a room with two doors in front of you. Would you enter door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There is a bear eating a cheese cake. What would you do?"
    print "1. Take the cake.\n2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear cries!"
    elif bear == "2":
        print "The bear roars!"
    else:
        print "%s is not an option, the bear has eaten the cake, and you."% bear

elif door == "2":
    print "You meet a cult priest who preaches you about the Old God"
    print "1. You run away."
    print "2. You punch him in the face."
    print "3. You channel your inner magical power to launch a fireball at him."

    insanity = raw_input("> ")
    if insanity == "1" or insanity == "2":
        print "The priest now treats you as the new Old God!"
    elif insanity == "3":
        print "Wow, I don't know you are a mage."

else:
    print "The walls close in and you become a pile of meat."
