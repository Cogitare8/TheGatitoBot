import discord
import time
import os
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Strong in the force, I am.')
    
@client.event
async def on_message(message):
    if len(message.content) == 9 and message.content[0:6] == message.content[0:6].upper():
        await message.channel.send(f'@everyone Kod: ' + message.content[0:6].rjust(12))
        await message.channel.send(f'@everyone Server: ' + message.content[7:9].upper().rjust(4))
        await message.channel.send(f'@everyone Host: ' + (str(message.author))[0:-5].rjust(13))
    elif len(message.content) == 6 and message.content[0:6] == message.content[0:6].upper():
        await message.channel.send(f'@everyone Kod: ' + message.content[0:6].rjust(10))
        await message.channel.send(f'@everyone Host: ' + (str(message.author))[0:-5].rjust(10))        
    
    if 'gatito' in message.content:
        await message.channel.send(f'*All hail the mighty Gatito*')
        
    if message.content == 'stfu':
        stfu = True
        print('1')
    
    if message.content.startswith('.spam'):
        stfu = False
        y = 1
        number = -2
        p = 0
        messageEnd = 0
        messageStart = 0
        delay = 0

        # Hur många gånger?
        try:
            temp = int(message.content[-2])
        except ValueError:
            x = int(message.content[-1])
            y = 0
        
        if y == 1:
            x = int(message.content[-2])*10 + int(message.content[-1])

       # Kolla efter var meddelandet börjar
        for u in message.content:
            if (u=='"' or u=='”'):
                messageStart = p
                break
            p += 1

        # Kolla efter var meddelandet slutar
        for u in range (p+1, len(message.content)):
            if (message.content[u] == '"' or message.content[u] == '”'):
                messageEnd = u
                break

        # Delay
        delay = int(message.content[messageEnd + 2])
            
        if(x<41):
            for z in range (0, x):
                if stfu == True:
                    print('2')
                    break
                await message.channel.send(message.content[messageStart+1:messageEnd])
                time.sleep(delay)
        else:
            await message.send(f'Balls')
    

client.run(os.environ['TOKEN'])
