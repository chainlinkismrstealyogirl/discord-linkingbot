import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import requests
import json
from replit import db
import random
from keep_alive import keep_alive
from discord import client

client = discord.Client()


# Startup Information
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='poop in the toilet'))

    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

balls_lmao = ["among" ,"among us"]

balls_lmao_reply = [
  "ok",
  "balls"
]

intercourse_cmd = ["intercourse"]

intercourse_reply = [
  "no",
  "no",
  "no",
  "stop",
  "stop",
  "stop",
  "go away",
  "go away",
  "go away",
  "sure bbg :smirk:"
]



@client.event
async def onready():
  print('sup {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('i love kastless'):
    await message.channel.send('shut up')

  if message.content.startswith('poop'):
    await message.channel.send('poop') 

  if message.content.startswith('*help'):
    await message.channel.send('commands: *help: shows commands - *poop: says poop - beatbox: sends thanos beatbox gif - intercourse: no - god: whatr?')

  if message.content.startswith('beatbox'):
    await message.channel.send('https://c.tenor.com/mjQ2uj8QuJQAAAAd/thanos-beatbox.gif%27')

  if message.content.startswith('*god'):
    await message.channel.send ('https://i.imgur.com/pUUlekN.mp47')
 
  if any(word in msg for word in balls_lmao):
    await message.channel.send(random.choice(balls_lmao_reply))
 
  if any(word in msg for word in intercourse_cmd):
    await message.channel.send(random.choice(intercourse_reply))

keep_alive()
#.env isn't public because it has the token :troll:
client.run(os.environ['TOKEN'])
