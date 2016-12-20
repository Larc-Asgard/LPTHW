class Scene(object):
    def __init__(self, title, urlname, description, helps, option1, option2, option3, option4, img):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}
        self.helps = helps
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.img = img
        
    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)




# Create the scenes of the game
armory = Scene("Armory", "armory",
"""
A creature has boarded the ship...It is hostile, ferocious and had killed one of your
crew memeber by brusting out of his chest. The ship has been set to denotate itself to eliminate the creature.
Now you are in the armory preparing your escape.
In front of you, there are four equipment you can choose from:
A pistol, a motion detector, an electroshock weapon and a flamethrower.
""",
"a pistol - a lethal and precise weapon on board; a motion detector - works like a radar, allowing you to sense movement near you; an electroshock weapon - good for stunning organism; a flamethrower - devastating instrument that can remove most of the non-metallic things on your path.",
'a pistol', 'a motion detector', 'an electroshock weapon', 'a flamethrower','armory.jpg')

motion_detected = Scene("Corridor", "monster_sighted",
"""
You step out of the corridor with the motion detector. It indicates that something is moving...
in front of you. But you don't see anything at all. Which way should you go?
""",
"front - despite of the anomaly on the detector; left - to the service Tunnel; right - to the canteen; back - to the armory;",
'to the front', 'to the left', 'to the right','go back', 'corridor.jpg')

monster_sighted = Scene("Corridor", "monster_sighted",
"""
You step out of the corridor. Making haste toward to escape shuffle, something
creeping above you...you slow down, a monstrous figure slide down to the corridor agilely.
It hasn't spot you yet. What would you do?
""",
"attack - perhaps you can bring it down with your weapon; left - to the service Tunnel; right - to the canteen; back - to the armory;",
'attack', 'to the left', 'to the right','go back', 'monster_sighted.png')

droid = Scene("The Service Tunnel", "droid",
"""
You sneak into the service tunnel where enginners do the maintenance tasks.
It is illumated by the red light as usual. You hope to seek Ash, the enginner of Nostromo
who might have survived this. When you finally encounter him, you call upon his name and he turns.
Something isn't right about this British man. His eyes seem to be glowing red.
You are not sure if you are so terrified or it is due to the lights.
As he approaches, you...
""",
"attack - he act so supcious, maybe hosted an extraterrestrial parasite; question - a civilized way to solve a potential criss; run - Since you are hunted by a monster, ignoring other questions as surival is the most importmant; approach - it might just because of the adrenaline, Ash has always been kind.",
'attack','question','runaway','get close', 'servicetunnel.jpg')

droid_killed = Scene("Escape Shuffle", "droid_killed",
"""
You must have been out of your mind. You attacked Ash.
But it was proven that you were right to as it was revealed that Ash is a droid.
Now you have made it to the deck to the shuffle.
But the terrifying creature is standing between you and the airlock.
Just one more obstacle between you and going home in one piece.
What would you do?
""",
"hold tight and open the airlock breifly - have you ever use a vaccum cleaner?; attack - it is living which means it can be killed; sneak - it doesn't seem to notice you yet; run - there are other shuffles aboard",
'open the airlock','attack','sneak','escape', 'droid_killed.jpg')


escape_pod = Scene("Escape Shuffle", "escape_pod",
"""
You have made it to the deck to the shuffle.
But the terrifying creature is standing between you and the airlock.
Just one more obstacle between you and going home in one piece.
What would you do?
""",
"hold tight and open the airlock breifly - have you ever use a vaccum cleaner?; attack - it is living which means it can be killed; sneak - it doesn't seem to notice you yet; run - there are other shuffles aboard",
'open the airlock','attack','sneak','escape','escapeshuffle.jpg')

the_end_winner = Scene("You Are Going Home", "the_end_winner",
"""
The airlock is opened and the void of space sucks that bastard out.
You close the airlock, catch your breath, realizing you have survived.
The creature is dead. The rest of the crew also. But you, survive.
And with the organic sample you collected, it might help develop a weapon or spot a weakness of that monster
before its kind steps on the soil of Earth.
But these, are the things for years later. You slowly walk toward to cryosleep chamber, exhausted.
You submerge yourself underneath the chilling water, prepared to finish the long interstellar journey in a long nap.
""",
None,None,None,None,None,None)


generic_death = Scene("Death...", "death", "You died.",
None,None,None,None,None,None)

eaten_death = Scene("You Died", "death", """
You rush to the other shuffle, nothing is here. Good.
Suddenly something fall from the above, pinning you on ground.
A abrupt pain rushes from you abdomen...The crawl of this 'thing' goes through you.
You bleed to death, but faint before you can see the creature.
""",
None,None,None,None,None, 'eaten.jpg')

sneak_failed = Scene("You Died", "death", """
You try to sneak pass the beast. The airlock is right in front of you.
You pull down the level and the airlock starts to pressurize.
But the sound draws the beast's attention! Shit...
You pray that the gate is opened before it comes...
It steps closer and closer. The roar gets louder and louder...
A abrupt pain rushes from you abdomen...You look down. The crawl of this 'thing' goes through you.
You bleed to death, but faint before you can see the creature.
""",
None,None,None,None,None, None)
ignore_signal = Scene("You Died", 'death',
"""
You walk up ahead, nothing is here. Maybe the dot is yourself displaced on the radar?
Suddenly something fall from the above, pinning you on ground.
A abrupt pain rushes from you abdomen...The crawl of this 'thing' goes through you.
You bleed to death, but faint before you can see the creature.
""",
None,None,None,None,None, None)

back_armory = Scene("You Died", 'death',
"""
You slowly walk back to the armory. Waiting the monster to walk away.
After a few moments, you try to open the hitch but it won't budge.
It seems like you are locked here. Well, at least you take that bastard with you.
The ship detonates as you set.
""",
None,None,None,None,None, 'armory.jpg')

canteen = Scene("You Died", 'death',
"""
You walk into the canteen, no one is here.
Suddenly something fall from the above, pinning you on ground.
A abrupt pain rushes from you abdomen...The crawl of this 'thing' goes through you.
You bleed to death, but faint before you can see the creature.
""",
None,None,None,None,None, 'canteen.jpg')

droid_question = Scene("You Died", "death",
"""
"Ash? Are you ok?"
"Yes, I am fine."
His voice is...robotic? A droid! He is a droid! But why is he here?\n
"Are you a droid?"\n
"I'm afraid I can't tell you that."\n
That's pretty obvious.\n
"I order you to reveal your purpose!"\n
"Access Denied."\n
He approaches with eyes iluminating threatening red. You try to raise your weapon, but too late to do so.
He put his hands around your neck and squeezes you to death.
""",
None,None,None,None,None, 'driod_attack.png')

droid_approach = Scene("You Died", "death",
"""
A living fellow crew member is a welcome sight. You approach him and share you plan of escaping the ship.
"Why would you want to?" he asks. You tell him that you have set the detonation of the engine,
neither them or the monster would survive if they stay on board.
"Well," he put his hands around your neck, "My job is to secure the payload to my master."
His voice is...robotic? A droid! He is a droid sent by your employer to ensure they can have the monster!
You can't breath...and slowly, slowly die...
""",
None,None,None,None,None, 'driod_attack.png')

attack_monster = Scene("You Died", 'death',
"""
You attempt to attack the creature in front of you. It seems to work!
Wait...it is merely confused at what is happening. Now it slowly approaches you.
Fear takes over your legs. It towers over you, lays its hands on your shoulders with great force.
It gets closer and closer...and it strikes out its touge into your mouth!
Something goes down into your chest, tearing it from the inside.
Pain is all you can feel, before you join the rest of crew...in death.
""",
None,None,None,None,None, 'eaten.jpg')



# Define the action commands available in each scene
the_end_winner.add_paths({
    '1': motion_detected,
    '2': droid,
    '3': escape_pod
})

escape_pod.add_paths({
    '1': the_end_winner,
    '2': attack_monster,
    '3': sneak_failed,
    '4': eaten_death
})

droid_killed.add_paths({
    '1': the_end_winner,
    '2': attack_monster,
    '3': sneak_failed,
    '4': eaten_death
})

droid.add_paths({
    '1': droid_killed,
    '2': droid_question,
    '3': escape_pod,
    '4': droid_approach,
})

monster_sighted.add_paths({
    '1': attack_monster,
    '2': droid,
    '3': canteen,
    '4': back_armory
})

motion_detected.add_paths({
    '1': ignore_signal,
    '2': droid,
    '3': canteen,
    '4': back_armory
})


armory.add_paths({
    '1': monster_sighted,
    '2': motion_detected,
    '3': monster_sighted,
    '4': monster_sighted
})


# Make some useful variables to be used in the web application
SCENES = {
    armory.urlname : armory,
    motion_detected.urlname : motion_detected,
    monster_sighted.urlname : monster_sighted,
    droid.urlname : droid,
    escape_pod.urlname : escape_pod,
    the_end_winner.urlname : the_end_winner,
    generic_death.urlname : generic_death,
    back_armory.urlname: back_armory,
    canteen.urlname: canteen,
    ignore_signal.urlname: ignore_signal,
    attack_monster.urlname: attack_monster,
    droid_question.urlname: droid_question,
    droid_killed.urlname: droid_killed,
    droid_approach.urlname: droid_approach,
    sneak_failed.urlname: sneak_failed
}

START = armory
