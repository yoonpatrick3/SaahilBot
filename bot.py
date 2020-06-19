import discord
from discord.ext import commands
import random
import time
import asyncio
import os
import re
from firebasedb import get_counter, update_counter, set_link, get_fb_link
#import pynacl

client = commands.Bot(command_prefix = 'kumar ')

client_token = 'NzIwNzkwMzg2MzM5MDg2MzUx.XuwgWQ.SVz4hcRge9AkX5vHekdVXfYTzx4'

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

saahilID = 267871956844412928
patID = 391344148738998273
botID = 720790386339086351
work_channel_id = 720745806939815997
groovy_channel_id = 720671297633517628
general_channel_id = 720670834561253489
debug_channel_id = 721143621536972951

def get_groovy_message(msg):
    if "-join" in msg.lower():
        return "GroovyBot will join when he wants to >:("
    elif "-p" in msg.lower():
        return "Dude what is your song choice..."
    elif "-skip" in msg.lower():
        return "Why are you skipping man"
    elif "-pause" in msg.lower():
        return "Don't pause my waifu GroovyBot"
    elif "-disconnect" in msg.lower():
        return "WHY DID U MAKE GROOVYBOT LEAVE <:PepeHands:720675250467242065>"
    else:
        update_counter()
        return "Shut up Saahil <:WeirdChamp:720710138759086080>"

@client.event
async def on_ready():
    print('The Sastillenator is ready to roll')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_message(message):
    if int(message.author.id) == saahilID:
        if int(message.channel.id) == general_channel_id or int(message.channel.id) == debug_channel_id:
            print("in here")
            update_counter()
            await message.channel.send("Shut up Saahil <:WeirdChamp:720710138759086080>")
        elif int(message.channel.id) == groovy_channel_id:
            await message.channel.send(get_groovy_message(message.content))
    await client.process_commands(message)

@client.command()
async def catch(ctx):
    await ctx.send('I caught it!')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["Sorry, can't answer right now. I'm jamming with Irene.",
                "Wait lemme walk Bubba first.",
                "Just ask Stanley, he's got all the answers.",
                "That is a Pepega question KEKG",
                "Classic",
                "You know I got a 100 on that last exam. Gotta keep flexing",
                "Sounds good babe <3",
                "hmm not sure",
                "uhh gimme a sec",
                "uhh sorry bb im talking to irene",
                "yikes",
                "i cry",
                "p cool question. too bad idk the answer to it",
                "ahh lemme ask irene first",
                "kk sounds good"]

    choices = random.choice(responses)

    await ctx.send(choices)

@client.command()
async def counter(ctx):
    counterMessage = "The Saahil Shut Up Counter: " + str(get_counter())
    await ctx.send(counterMessage)

@client.command()
async def fuck(ctx):
    await ctx.send("<:D_:720827719788658758>")

@client.command(aliases=['great'])
async def good(ctx):
    await ctx.send("hehe thanks bb <3 <:PepeLove:720828348103786517>")

def getLinkInformation(lines):
    desc = ""
    link = ""
    for l in lines:
        if re.match(regex, l):
            link = l
        else:
            desc += l
            desc += " "
    
    return desc, link[:-1]

@client.command()
async def save_link(ctx, *args):
    try:
        desc, link = getLinkInformation(args)
        set_link(desc, link)
        await ctx.send("Saved successfully <:PepeYes:721145634454765628>")
    except:
        await ctx.send("SaahilBot broke yieks")


@client.command()
async def get_link(ctx, *, args):
    descArray, linkArray = get_fb_link(args)
    if len(descArray) == 0:
        await ctx.send("Couldn't find that description <:FeelsBadMan:721147885588054095>")
    else:
        for i in range(len(descArray)):
            await ctx.send(descArray[i] + " " + linkArray[i])

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def shut(ctx):
    await ctx.send("Shut up Saahil WeirdChamp", tts=True)

client.run(client_token)