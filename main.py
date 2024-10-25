import configuration as conf

class Hero():
    def __init__(self, name):
        self.name = name
        self.health = conf.HEALTH
        self.attack_power = conf.ATTACK_POWER

    def attack(self,other):
        pass

    def is_alive(self):
        pass

class Game():
    def __init__(self, player:Hero(), computer:Hero()):
        self.player = player
        self.computer = computer

    def start(self):
        pass
