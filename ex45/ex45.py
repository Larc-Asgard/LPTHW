from sys import exit
from random import randint
#putting all the monsters into one document
from ex45_minion import Minion, FireMinion, WaterMinion, EarthMinion, WindMinion

#for organizational reason
class Boss(object):
    pass
#parent
class Stage(object):
    def enter(self):
        print "This stage is currently empty."
        exit(1)
#the "runner", ref to ex43
class Engine(object):
    def __init__(self, stage_map):
        self.stage_map = stage_map

    def play(self):
        current_stage = self.stage_map.opening_stage()
        last_stage = self.stage_map.next_stage('finished')

        while current_stage != last_stage:
            next_stage_name = current_stage.enter()
            current_stage = self.stage_map.next_stage(next_stage_name)

        current_stage.enter()

class GGWP(Stage):
    def enter(self):
        print "Game Over."
        exit(1)

#player class, nothing but a HP bar
class Player(object):
    def __init__(self):
        self.health = 5
#randomize the boss
class Dragon(Boss):

    def __init__(self):
        self.health = 5
        lottery = randint (1,4)
        if  lottery == 1:
            self.element = "Fire"
            self.ability = "Blast Burn"
        elif lottery == 2:
            self.element = "Water"
            self.ability = "Hydro Cannon"
        elif lottery == 3:
            self.element = "Earth"
            self.ability = "Rock Tomb"
        elif lottery == 4:
            self.element = "Wind"
            self.ability = "Hurricane"
        element = self.element
        self.name = element + " Dragon"
        name = self.name

class Entrance(Stage):

    def enter(self):
        print "You are a powerful wizard who controls 4 different elements."
        print "They are: Fire, Water, Earth and Wind."
        print "Each of them has a weakness:"
        print "Fire is extinguished by Water;"
        print "Water is blocked by Earth."
        print "Earth is blown into sand by Wind."
        print "Wind is burnt out by Fire."
        print "These rules of nature would help you defeat the monsters lurking in the dungeon in front of you."
        print "Are you ready? (y/n)"

        ready = raw_input("> ")
        if ready == "y":
            floor = 1
            return "EarlyStair"
        elif ready == "n":
            "Farewell."
            exit(1)
#what special about this game is, every playthrough is different
#the monsters are randomly generated
class EarlyStair(Stage):

    def __init__(self):
        pass
    def enter(self):
        print "You are in the 1st level of the dungeon."
        lottery = randint (1,4)
        if lottery == 1:
            monster = FireMinion("Fire Spark")
        if lottery == 2:
            monster = WaterMinion("Water Drops")
        if lottery == 3:
            monster = EarthMinion("Sand")
        if lottery == 4:
            monster = WindMinion("Breeze")

        print "A %s appears!"% monster.name
        print "You cast:\n1. Fireball\n2. Frost Bolt\n3. Rock Rocket\n4. Wind Blade"
        spell = raw_input("> ")

        if spell == "1":
            spellkill = "Wind"
        elif spell == "2":
            spellkill = "Fire"
        elif spell == "3":
            spellkill = "Water"
        elif spell == "4":
            spellkill = "Earth"
        else:
            print "Your spell is casted in a wrong way. The monster gets you."
            GGWP().enter()


        if spellkill == monster.element:
            print "You have killed the monster!"
            print "You walk down the stair guarded by the %s"%monster.name
            return 'MidStair'

        else:
            print "It is not effective..."
            print "The %s attacks you and flees."% monster.name
            player.health = player.health - 1
            print "Lose one health."
            print "Currect health: %d"% player.health
            print "You continue to explore."
            return 'EarlyStair'

        if player.health == 0:
            GGWP().enter()
#pretty much the same as EarlyStair()
class MidStair(Stage):

    def __init__(self):
        pass
    def enter(self):
        print "You are in the 2nd level of the dungeon."

        lottery = randint (1,4)
        if lottery == 1:
            monster = FireMinion("Flame")
        if lottery == 2:
            monster = WaterMinion("Tidal")
        if lottery == 3:
            monster = EarthMinion("Rocky")
        if lottery == 4:
            monster = WindMinion("Whirlwind")
        print "A %s appears!"% monster.name
        print "You cast:\n1. Fireball\n2. Frost Bolt\n3. Rock Rocket\n4. Wind Blade"
        spell = raw_input("> ")

        if spell == "1":
            spellkill = "Wind"
        elif spell == "2":
            spellkill = "Fire"
        elif spell == "3":
            spellkill = "Water"
        elif spell == "4":
            spellkill = "Earth"
        else:
            print "Your spell is casted in a wrong way. The monster gets you."
            GGWP().enter()


        if spellkill == monster.element:
            print "You have killed the monster!"
            print "You walk down the stair guarded by the %s"%monster.name
            return "EndStair"
        else:
            print "It is not effective..."
            print "The %s attacks you and flees."% monster.name
            player.health = player.health - 2
            print "Lose two health."
            print "Currect health: %d"% player.health
            print "You continue to explore."
            return "MidStair"

        if player.health == 0:
            GGWP().enter()
#pretty much the same as EarlyStair()
class EndStair(Stage):

    def __init__(self):
        pass

    def enter(self):
        print "You are in the 3rd level of the dungeon."

        lottery = randint (1,4)
        if lottery == 1:
            monster = FireMinion("Lava")
        if lottery == 2:
            monster = WaterMinion("Tsunami")
        if lottery == 3:
            monster = EarthMinion("Boulder")
        if lottery == 4:
            monster = WindMinion("Typhoon")
        print "A %s appears!"% monster.name
        print "You cast:\n1. Fireball\n2. Frost Bolt\n3. Rock Rocket\n4. Wind Blade"
        spell = raw_input("> ")

        if spell == "1":
            spellkill = "Wind"
        elif spell == "2":
            spellkill = "Fire"
        elif spell == "3":
            spellkill = "Water"
        elif spell == "4":
            spellkill = "Earth"
        else:
            print "Your spell is casted in a wrong way. The monster gets you."
            GGWP().enter()

        if spellkill == monster.element:
            print "You have killed the monster!"
            print "You walk down the stair guarded by the %s"%monster.name
            return "FinalStage"
        else:
            print "It is not effective..."
            print "The %s attacks you and flees."% monster.name
            player.health = player.health - 3
            print "Lose three health."
            print "Currect health: %d"% player.health
            print "You continue to explore."
            return "EndStair"

        if player.health == 0:
            GGWP().enter()
#actually I think that the combat part can be put into one class/function
#so that each map will only call upon the function whenever player has encountered a monster
#but I'm not very familiar with throwing varaibles across classes/functions
class FinalStage(Stage):

    def __init__(self):
        pass

    def enter(self):
        print "You have reached the end of the stair..."
        print "Here is where the notorious dragon rest..."
        print "You carefully approach the shadow in front of you until it reveals itself."
        print "It is a %s!!"%boss.name
        print "Fear not, Great Mage! Magic is at your disposal!"
        print "You cast:\n1. Fireball\n2. Frost Bolt\n3. Rock Rocket\n4. Wind Blade"
        spell = raw_input("> ")


        if spell == "1":
            spellkill = "Wind"
        elif spell == "2":
            spellkill = "Fire"
        elif spell == "3":
            spellkill = "Water"
        elif spell == "4":
            spellkill = "Earth"
        else:
            print "Your spell is casted in a wrong way. The dragon gets you."
            GGWP().enter()

        if spellkill == boss.element:
            boss.health = boss.health - 1
            print "You have hurted the Dragon!"
            print "But it's about to attack!"
            print "Cast the same element to neutralize the attack!"
            print "The Dragon uses %s!!" %boss.ability
            print "You cast:\n1. Fireball\n2. Frost Bolt\n3. Rock Rocket\n4. Wind Blade"
            spell = raw_input("> ")



            if spell == "1":
                spellelement = "Fire"
            elif spell == "2":
                spellelement = "Water"
            elif spell == "3":
                spellelement = "Earth"
            elif spell == "4":
                spellelement = "Wind"
            else:
                print "Your spell is casted in a wrong way. The dragon gets you."
                GGWP().enter()

            if spellelement == boss.element:
                boss.health = boss.health - 1
                print "Now you have the chance to end this beast once and for all!"
                print "You gather all your strength into this spell..."
                print "You cast:\n1. Pyroblast\n2. Blizzard\n3. Earth Shock\n4. Lightning Storm"
                spell = raw_input("> ")


                if spell == "1":
                    spellkill = "Wind"
                elif spell == "2":
                    spellkill = "Fire"
                elif spell == "3":
                    spellkill = "Water"
                elif spell == "4":
                    spellkill = "Earth"
                else:
                    print "Your spell is casted in a wrong way. The dragon gets you."
                    GGWP().enter()

                if spellkill == boss.element:
                    print "You have defeated the dragon!"
                    return "finished"
                else:
                    print "The spell has no effect on its scale. The dragon swings it's claw upon you..."
                    return "GameOver"
            else:
                print "The spell has no effect on its scale. The dragon swings it's claw upon you..."
                return "GameOver"
        else:
            print "The spell has no effect on its scale. The dragon swings it's claw upon you..."
            return "GameOver"
class Winning(Stage):
    def enter(self):
        print "You have defeated all the monsters in this dungeon."
        print "Farewell! Hero."

#ref to ex43
class Level(object):
    stages = {

        'Entrance': Entrance(),
        'EarlyStair': EarlyStair(),
        'MidStair': MidStair(),
        'EndStair': EndStair(),
        'FinalStage': FinalStage(),
        'finished': Winning(),
        "GameOver": GGWP()

    }
    def __init__(self, start_stage):
        self.start_stage = start_stage

    def next_stage(self, stage_name):
        val = Level.stages.get(stage_name)
        return val

    def opening_stage(self):
        return self.next_stage(self.start_stage)


#actual running code, ref to ex43
player = Player()
boss = Dragon()
a_map = Level("Entrance")
a_game = Engine(a_map)
a_game.play()
