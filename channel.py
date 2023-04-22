# For personal channel
import discord
import os 
from dotenv import load_dotenv

client = discord.Client('0')
botPrefix = "!bot" 

@client.event
async def on_ready():
    print('We have logged in as {0.user}' .format(client))