#!/usr/bin/env python3

class Monster():
    def __init__(self, name, description, hp, damage):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage

    def __str__(self):
        return "{}\n======================\n{}\nHP: {}".format(self.name, self.description, self.hp)

    def isalive(self)
    """
    returns true if hp > 0
    """
    return self.hp > 0



############ monsters ################3

class Kasper(Monster):
    def __init__(self):
        super().__init__(name = "Kasper The Unfriendly Ghost", description = "Clearly a hellspawn beast, repulsive to the eyes.  Whispers surround you \"...subnetting...\"", hp = 100, damage = 10)
