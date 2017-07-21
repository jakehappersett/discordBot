#!/usr/bin/env python3

import discord
import asyncio
from player import Player
from Bot import ChatBot
from random import randint, choice

class SaundersBot(ChatBot):
    """
    
    Discord bot with basic functionalities, 
    created mostly to mess with my friends
    
    """
    STATUS = "Fuck you, Nat"
    client = discord.Client() 
    
    def __init__(self, name):
        super(SaundersBot, self).__init__(name)
    CHARDICT = {}

    #############test function ####################

    @ChatBot.action()
    async def test(self,args,mobj):
        """
        function just for tests
        """

        return await self.message(mobj.channel, type(args))



    ###############################################

    @ChatBot.action('[Users]')
    async def charcreate(self, args, mobj):
        """
        Creates player
        """
        ids = [self.convert_user_tag(x) for x in args]
        for uid in ids:
            if uid is not False:
                #to return a username : 
                #myid = '<@' + uid + '>'
                name = discord.Server.get_member(mobj.server, uid)
                self.CHARDICT.update({uid:Player(str(name))})
                a = self.CHARDICT[uid]
        return await self.message(mobj.channel, a.name + ' has been created')

    @ChatBot.action()
    async def inventory(self, args, mobj):
        """
        access inventory
        """
        player = self.CHARDICT[mobj.author.id]
        return await self.message(mobj.channel, player.printinv())

    @ChatBot.action()
    async def addinventory(self, args, mobj): 
        """
        add to inventory
        """
        player = self.CHARDICT[mobj.author.id]
        #joins arguments for multi word items (i.e. sword of anal destruction)
        jargs = ' '.join(args)
        player.addinv(jargs)
        return await self.message(mobj.channel, str(args) + ' successfully added to inventory \nnew inventory : ' + player.printinv())

    @ChatBot.action()
    async def fucknat(self, args, mobj):
        """
        Put Nat in his place
        Example: !fucknat
        """
        return await self.message(mobj.channel, "Fuck you, Nat")

    @ChatBot.action()
    async def choice(self, args, mobj):
        """
        Make a decision
        Example: !choice
        """
        return await self.message(mobj.channel, choice(["<:gasaunde:293500522550525954>", "<:downsaunder:294248046357905410>"]))


if __name__ == "__main__":
        s = SaundersBot("saunders")
        s.run()
        pass

