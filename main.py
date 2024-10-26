import configuration as conf
import random as r

class Hero():
    def __init__(self, name):
        self.name = name
        self.health = conf.HEALTH
        self.attack_power = conf.ATTACK_POWER

    def attack(self,other):
        if self.name == "computer":
            self.attack_power = r.randint(conf.ATTACK_POWER,conf.ATTACK_POWER ** 5)
        other.health -= self.attack_power

    def is_alive(self):
        if self.health > 0:
            return True
        return False

class Game():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        pass

def test_attack_is_alive():
    hero1 = Hero("Nina")
    hero2 = Hero("computer")
    print(hero1.health)
    print(hero2.health)
    while hero1.health > 0 and hero2.health > 0:
        print("Первый атакует")
        hero1.attack(hero2)
        print(f"hero1 - {hero1.health}")
        print(hero1.is_alive())
        print(f"hero2 - {hero2.health}")
        print(hero2.is_alive())
        print("Комп атакует")
        hero2.attack(hero1)
        print(f"hero1 - {hero1.health}")
        print(hero1.is_alive())
        print(f"hero2 - {hero2.health}")
        print(hero2.is_alive())

    #тестирование метода attack
test_attack_is_alive()
# game = Game()
# game.start()
