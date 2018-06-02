#https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import random

TOKEN = 'NDUyMTE0MzUwNDg0ODgxNDE4.DfLn0Q.zbGTmcJOYDjystjydtf_1YccShs'

client = discord.Client()
creator_id = '<@342078340301062145>'
owner_id = '<@404303531466817536>'

@client.event
async def on_member_join(member):
    await client.send_message(client.get_channel('406173616649011201'), f'Hey {member.mention}, welcome to the server for \"The Scarlet Speedster: A Flash Fangame\"!')

@client.event
async def on_message(message):
        # we do not want the bot to reply to itself
    if message.author == client.user:
        return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
