from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int (choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greddy, you win!"
        exit(0)
    else:
        dead("you greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "It has a bunch of honey."
    print "The fat bear is sitting in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
def oldgod_room():
    print "Here you see the evil Old God."
    print "Yogg-Saron looks at you and you start to go insane into his lucid dream"
    print "Fight, or flight?"
    choice = raw_input("> ")
    if "flight" in choice:
        start()
    elif "fight" in choice:
        dead("He is too powerful!")
    else: oldgod_room()

def dead(why):
    print why, "You are dead!"
    exit(0)

def start():
    print "There are two doors in front of you."
    print "Left, or right?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        oldgod_room()
    else:
        dead("The walls close in.")

start()
