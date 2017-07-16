#!/usr/bin/env python3

class Item():
    """
    Base class for items
    """
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def __str__(self):
        return "{}\n======\n{}Value: {}\n".format(self.name, self.description, self.value)


################ Items (note : NOT weapons) ##########################

class Gold(Item):
    """
    Gold is a subclass of the superclass item 
    """
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name = "Gold", description = "A tarnished round coin, you can make out faint initials engraved on the coin \"A.J.W\"", value = self.amt)

####################### Weapons #####################################

class Weapon(Item):
    """
    Class for weapons, inherits from items but adds damage attribute.  
    Made to make weapon creation simpler, also adds str with damage 
    """
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name,dsecription, value)
    def __str__(self):
        return "{}\n======\n{}Value: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock", description = "Grey and round, would probably hurt a bit to get hit by it", value = 0, damage = 5)

class SaunderSword(Weapon):
    def __init__(self):
        super().__init__(name="Saunder Sword", description = "Large two handed sword, makes the maids GUI", value = 100, damage = 10)
