#!/usr/bin/env python3

import discord
import asyncio
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

#
#client = discord.Client()
#@client.event
#async def on_ready():
#    print('Logged in as')
#    print(client.user.name)
#    print(client.user.id)
#    print('------')
#
#@client.event
#async def on_message(message):
#    if message.content.startswith('.test'):
#        counter = 0
#        tmp = await client.send_message(message.channel, 'Calculating messages...')
#        async for log in client.logs_from(message.channel, limit=100):
#            if log.author == message.author:
#                counter += 1
#
#        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
#    elif message.content.startswith('.sleep'):
#        await asyncio.sleep(5)
#        await client.send_message(message.channel, 'Done sleeping')
#    elif message.content.startswith('.ping'):
#        await client.send_message(message.channel, "Pong!")
#    elif message.content.startswith('.fucknat'):
#        await client.send_message(message.channel, "Fuck you, Nat")
#client.run('MzI5MzQwOTU1MzU2NTYxNDE5.DDRCSQ.P5dv1mvzh1Lz_uvL47F7ng9nG4c')
