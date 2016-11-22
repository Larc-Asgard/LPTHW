from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene is yet to be configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
    quips = [
    "You died."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "Your ship has been invaded and crew obliterated."
        print "You are on your own."
        print "Your hope lies onto setting up a bomb and then escape"
        print "You are on your way to the Armory, where the bomb locates."
        print "A alien monster is standing between you and your goal."
        print "So you..."

        action = raw_input("> ")

        if action == "shoot":
            print "The monster is hitted and spilling blood...acidic blood!"
            print "It corrodes your body and you are death."
            return "death"

        elif action == "dodge":
            print "The monster is so agile."
            print "You out run it only to find its tail has penetrated your chest..."
            print "death"

        elif action == "dance":
            print "You bust out some lame moves. The monster is confused."
            print "'What the heck is this human doing?'"
            print "You slip into the armory while it is confused."
            return "laser_weapon_armory"

        else:
            print "input: shoot/dodge/dance"
            return "central_corridor"

class LaserWeaponArmory(Scene):
    def enter(self):
        print "The bomb is in front of you."
        print "All you need to do it type in the correct code..."
        code = "%d%d%d"% (randint(1,9), randint(1,9), randint(1,9))
        print "Code: ", code
        guess = raw_input ("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BUZZ!"
            guesses += 1
            guess = raw_input ("[keypad]> ")

        if guess == code:
            print "It opens. Now you need to place it at the right spot..."
            return "the_bridge"

        else:
            print "Too many failed attempts!"
            print "Self-Detonation in..."
            return "death"

class TheBridge(Scene):
    def enter(self):
        print "You are at the bridge."
        print "The monsters seem to have established a nest near the window."
        print "But explosion at the panel would probably dismantel the ship completely."
        print "So you put the bomb at:"

        action = raw_input("> ")

        if action == "nest":
            print "You move to the nest. One of the many eggs brusts!"
            print "A monster larva is crawling at your face!"
            print "You can't breath...but the bomb has already set..."
            return "death"

        elif action == "panel":
            print "Surprisngly, nothing notice your actions."
            print "You slowly withdraw from the room and run to the escape pod."
            return "escape_pod"

        else:
            print "nest/panel"
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print "There are only two pods left."
        print "Left or right?"

        good_pod = randint(1,2)
        guess = raw_input("1 for left, 2 for right> ")

        if int(guess) != good_pod:
            print "You press the eject button...nothing happens"
            print "You are struck in it while the bomb goes off."
            return "death"

        else:
            print "You press the eject button...and all you can see is the space"
            print "After a seemingly never ending time, you see a familiar blue planet - Earth."

            return "finished"
class Finished(Scene):

    def enter(self):
        print "You won."
        return "finished"
class Map(object):

    scenes = {
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished':Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
