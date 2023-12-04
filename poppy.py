# Rust Bot v2.0
from bs4 import BeautifulSoup as bs
import requests
import discord
from discord.ext import commands
import urllib.request
import re
# import pandas as pd


#Discord Bot information
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(intents=intents , command_prefix = '!')

#Events
@client.event
async def on_ready():
    print('Hey there cuties. ;) xoxo')

@client.event
async def on_member_join(member):
    print(f'{member} has joined, what a cutie. ;)')

@client.event
async def on_member_remove(member):
    print(f"You're gonna carry that weight {member}.")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! :ping_pong: Latency:{round(client.latency * 1000)}ms')

@client.command()
async def moose(ctx):
    await ctx.send(f'Players Online:')

source = requests.get('https://moose.gg/ssm/').text
soup = bs(source, 'lxml')
#Parse for Moose Main info
main = soup.find('div', class_ = 'ipsColumn ipsColumn_fluid')
#Grabbing the "Online Players" line
early = main.findAll("p", style="margin-top:0")[2]
print(early)

#load html code from a url
# page = urllib.request.urlopen("https://moose.gg/servers")
# soup = bs(page)

# names = soup.body.findAll("p")
# function_names = re.findall("style=magin-top:0")

#Token
client.run('$TOKEN')
