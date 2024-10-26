import configuration as conf
import random as r

class Hero():
    def __init__(self, name):
        self.name = name
        self.health = conf.HEALTH
        self.attack_power = conf.ATTACK_POWER

    def attack(self,other):
        if self.name == "computer":
            self.attack_power = r.randint(conf.ATTACK_POWER,conf.ATTACK_POWER_max)
        other.health -= self.attack_power

    def is_alive(self):
        if self.health > 0:
            return True
        return False

class Game():
    def __init__(self,player,computer):
        self.player = player
        self.computer = computer

    def start(self):
        while hero1.is_alive() and hero2.is_alive():
            print(f"Игрок {hero1.name.upper()} атакует!")
            hero1.attack(hero2)
            print(f"Оставшееся здоровье компьютера  - {hero2.health}")
            print("Компьютер атакует!")
            hero2.attack(hero1)
            print(f"Оставшееся здоровье игрока {hero1.name.upper()}  - {hero1.health}")
        if hero1.is_alive() == False:
            print(f"Победа за {hero2.name.upper()}!!!")
        elif hero2.is_alive() == False:
            print(f"Победа за {hero1.name.upper()}!!!")


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
#test_attack_is_alive()

#текст игры
print("Игра БИТВА ГЕРОЕВ началась!")
hero1_name = input("Введите имя игрока: ")
hero1 = Hero(hero1_name)
hero2 = Hero("computer")
game = Game(hero1, hero2)
game.start()
