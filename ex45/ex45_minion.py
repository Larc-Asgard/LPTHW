class Minion(object):
    def __init__(self, element):
        self.element = None

class FireMinion(Minion):
    def __init__(self, name):
        self.name = name + " Minion"
        self.element = "Fire"

class WaterMinion(Minion):
    def __init__(self, name):
        self.name = name + " Minion"
        self.element = "Water"

class EarthMinion(Minion):
    def __init__(self, name):
        self.name = name + " Minion"
        self.element = "Earth"

class WindMinion(Minion):
    def __init__(self, name):
        self.name = name + " Minion"
        self.element = "Wind"
