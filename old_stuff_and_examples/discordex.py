#!/usr/bin/env python

import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    for ej in client.get_all_emojis():
        print(ej.name, ej.id, ej.managed, ej.server)

@client.event
async def on_message(message):
    if message.content.startswith('.test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('.sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('.ping'):
        await client.send_message(message.channel, "Pong!")
    elif message.content.startswith('.fucknat'):
        await client.send_message(message.channel, "Fuck you, Nat")
client.run('MzI5MzQwOTU1MzU2NTYxNDE5.DDRCSQ.P5dv1mvzh1Lz_uvL47F7ng9nG4c')
