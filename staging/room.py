#!/usr/bin/env python3


#todo : 
#    decide where reward should be 
#    create reward logic

class room():
    def __init__(self, rmtype, description,reward)
    self.rmtype = rmtype
    self.description = description
    ##should this be in moster or room?
    self.reward = reward
    

###################### Room Types ############################

class encounter(room):
    self.rmtype = "encounter"
    self.desc = "somethin\' scurry is here"
    self.reward = 10

class empty(room):
    self.rmtype = "empty"
    self.desc = "ain\'t nothin here"
    self.reward = 0
