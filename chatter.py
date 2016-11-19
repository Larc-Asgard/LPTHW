#this has both composition and inheritance 

class Chatter(object):

    def __init__(self):
        self.emotion = None

    def start(self, startemo):
        self.emotion = startemo
        print "Hello, what would you like to talk about?"
        userinput = raw_input(">> ")

        while userinput != "quit":

            if "angry" in userinput:
                self.emotion = Angry()

            elif "silly" in userinput:
                self.emotion = Coy()

            elif "hi" in userinput:
                self.emotion = Welcoming()

            print self.emotion.respond(userinput)
            userinput = raw_input(self.emotion.ifeel() + ">> ")



class Emotion(object):

    def __init__(self, feeling):
        self.feeling = feeling

    def ifeel(self):
        return "I feel %s"% self.feeling

class Angry(Emotion):

    def __init__(self):
        super(Angry, self).__init__("angry")

    def respond(self, userinput):
        if "good" in userinput:
            return "I don't care if you're good."
        elif "bad" in userinput:
            return "Good, I'm glad that things' bad."
        elif "hello" in userinput:
            return "Fuck off."
        else:
            return "What the fuck do you want?"

class Welcoming(Emotion):

    def __init__(self):
        super(Welcoming, self).__init__("welcoming")

    def respond(self, userinput):
        if "good" in userinput:
            return "I'm happy for you."
        elif "bad" in userinput:
            return "I wish you the best!"
        elif "hello" in userinput:
            return "Oh hello."
        else:
            return "Welcome to the world of programming!"

class Coy(Emotion):

    def __init__(self):
        super(Coy, self).__init__("coy")


    def respond(self, userinput):
        if "good" in userinput:
            return "Good? But the goodies are in the boobies."
        elif "bad" in userinput:
            return "Bad? I like baaaad boys."
        elif "hello" in userinput:
            return "Hello...that's all you gonna do?"
        else:
            return "How about a little actions?"

app = Chatter()
startemotion = Welcoming()
app.start(startemotion)
