from sys import exit

def fair():
    print "You can choose from:"
    print "1. Hera, the Queen of Gods"
    print "2. Athena, the Goddess of Wisdom and War"
    print "3. Aphrodite, the Goddess of Love, Beauty and Sexuality"

    choice = raw_input("> ")
    if choice == "1":
        print "Hera gets the Golden Apple! The world is now full of envy."
    elif choice == "2":
        print "Athena gets the Golden Apple! People start to realize the problem of their society."
        print "They rage wars against the oppressed."
    elif choice == "3":
        print "Aphrodite gets the Golden Apple! The world are full of beauties, but fools at the same time."
        print "Perhaps it is the best?"

def unfair():
    print "The candidates try to bribe you, they offered:"
    print "1. Power, rule over the entire land of Europe and Asia"
    print "2. Wisdom and skills that will win you any battle, and war"
    print "3. A true love with the most beautiful woman in the world."

    choice = raw_input("> ")
    if choice == "1":
        print "Hera gets the Golden Apple!"
        king()
    elif choice == "2":
        print "Athena gets the Golden Apple!"
        general()
    elif choice == "3":
        print "Aphrodite gets the Golden Apple!"
        print "And Helen appears in your life and you two fall in love..."
        print "But she is the wife of a Greek King Menelaus."
        print "You have started...the Trojan War."

def king():
    print "With the power on hand. What would you do?"
    print "1. Rule over as the greatest emperor ever!"
    print "2. Let the power goes, they belong to the people!"

    choice = raw_input("> ")
    if choice == "1":
        print "Without the wisdom, you people suffer, you empire shatters right after your death."
    elif choice == "2":
        print "People isn't really ready for democracy...But this noble act of giving up power has planted the seed in history."

def general():
    print "With wisdom and skills, where will you go?"
    print "1. To the most prosperous city"
    print "2. To the far east"

    choice = raw_input("> ")
    if choice == "1":
        print "You travelled to Rome...People in the future know you as Caesar"
    elif choice == "2":
        print "In the mysterious east, you meet an old man who gives you the oddest looking plant."
        plant()

def plant():
    print "1. Eat it."
    print "2. Refuse."

    choice = raw_input("> ")
    if choice == "1":
        print "You seem to never age. You are being known as many names...Han Xin, Zhao Yun..."
    elif choice == "2":
        print "You travel and learn every martial art you encountered. \nYou have created many on your own. People now called you 'Bodhidharma'"


def start():
    print "Eris, not getting invited to the banquet has set a discord to the world."
    print "You, Paris, would be the one who can perphas save it from disaster."
    print "You will have to choose, who is worthy of the Golden Apple."
    print "Fulfilling this duty, you will be rewarded by:"
    print "1. Nothing. But the Gods shall favor you."
    print "2. Power, wisdom or women."
    choice = raw_input("> ")

    if choice == "1":
        fair()
    elif choice == "2":
        unfair()
    else:
        exit(0)

start()
