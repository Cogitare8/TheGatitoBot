import discord
import time
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
albin = '248486917170135041'

@client.event
async def on_ready():
    print('Strong in the force, I am.')

@client.command()
async def gatito(ctx):
    await ctx.send(f'The <@248486917170135041>')

@client.command()
async def spam(ctx):
    y = 1
    number = -2
    p = 0
    messageEnd = 0
    messageStart = 0
    delay = 0

    # Hur många gånger?
    try:
        temp = int(ctx.message.content[-2])
    except ValueError:
        x = int(ctx.message.content[-1])
        y = 0
        
    if y == 1:
        x = int(ctx.message.content[-2])*10 + int(ctx.message.content[-1])

    # Kolla efter var meddelandet börjar
    for u in ctx.message.content:
        if (u=='"'):
            messageStart = p
            break
        p += 1

    # Kolla efter var meddelandet slutar
    for u in range (p+1, len(ctx.message.content)):
        if (ctx.message.content[u] == '"'):
            messageEnd = u
            break

    # Delay
    delay = int(ctx.message.content[messageEnd + 2])
        
    if(x<21):
        for z in range (0, x):    
            await ctx.send(ctx.message.content[messageStart+1:messageEnd])
            time.sleep(delay)
    else:
        await ctx.send(f'Balls')

@client.event
async def on_member_join(member):
    await member.channel.send(f'Tjena ' + member) 

    

client.run(os.environ['DISCORD_TOKEN'])
