#!/usr/bin/env python3

class Player():
    def __init__(self, name):
        self.name = name
        self.inventory = ['nat\'s head', 'louie\'s head']
        self.hp = 100
        self.level = 1 
    def __str__(self):
        return("{}\n======\nInventory: {}\nHP: {} \nLevel: {}".format(self.name, self.printinv(), self.hp, self.level))
    
    def addinv(self, args):
        """
        Add things to inventory, discord returns message arguments (args) as 
        list types so addinv tests the argument to see if it is a list and 
        appends inventory accordingly
        """
        if ((type(args) is list) == True):
            self.inventory = self.inventory + args
        elif ((type(args) is str) == True):
            self.inventory.append(args)
    def printinv(self):
        """
        converts inventory list to string to print
        """
        out ='[' + ', '.join(str(e) for e in self.inventory) + ']'
        return out
    def isalive(self):
        """
        returns true if hp > 0
        """
        return self.hp > 0

