from twitchio.ext import commands
import os
from discord import DISCORD_DIC
import re
import random

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL'], "qtmajestic", 'dudewood']
)

@bot.command(name='test')
async def test(context):
    await context.send("First Try!")
    

@bot.command(name='8ball')
async def eight_ball(context):
    options = [
        "As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes – definitely.",
        "You may rely on it.",
    ]
    if "the run" in context.content.split("!8ball")[-1].lower():
        answer = "yes"
    else:
        answer = options[random.randint(0, len(options)-1)]

    await context.send(answer)

@bot.command(name='so')
async def shout_out(context):
    shout_out = context.content.split("!so")[-1].strip()
    print(context.content)
    await context.send(f"Checkout {shout_out} at twitch.com/{shout_out}")
    pass

@bot.command(name='husbando')
async def husbando(context):
    await context.send("Berry's Husbando is Daruk's descendant, Yunobo. Kappa")
    pass

@bot.command(name='discord')
async def discord(context):
    discord_link = DISCORD_DIC.get(str(context.channel), None)
    if discord_link is not None:
        await context.send(f"Join the Discord: {discord_link}")
    else:
        await context.send("Sorry, I couldn't find the discord link for this channel ¯\_(ツ)_/¯")
    pass
    
@bot.event
async def event_ready():
    print(f"{os.environ['BOT_NICK']} is online!")
    # ws = bot._ws
    # await bot.handle_commands

@bot.event
async def event_message(context):
    if context.author.name.lower() == os.environ['BOT_NICK'].lower():
        return
    
    await bot.handle_commands(context)
    # print(context.channel)
    # print(teste)
    if 'we could make a religion out of this' in context.content.lower():
        await context.channel.send("no dont.")

    if 'hype' in context.content.lower():
        await context.channel.send("PogU")

    if 'pogu vladisbot' in context.content.lower() or 'pogyou vladisbot' in context.content.lower():
        await context.channel.send("PogMe? nah fam, PogYou")

    greets = [
        "hello vladisbot",
        "hi vladisbot",
        "hello chat",
        "hi chat",
        "hey vladisbot"
        # "howdy vladisbot",
        # "howdy chat",
    ]

    if "yunobo" in context.content.lower(): 
        await context.channel.send("Berry+Yunobo = <3")

    if any(i in context.content.lower() for i in greets):
        await context.channel.send(f"Hi, @{context.author.name}! KonCha")

    if any(i in context.content.lower() for i in ["howdy vladisbot", "howdy chat" ]):
        await context.channel.send("Howdy, partner!")

    if any(i in context.content.lower() for i in ["greetings vladisbot", 'greetings chat']):
        await context.channel.send(f"Greetings, @{context.author.name}! *tips hat*")
        pass

    if re.compile(r".*(?<![\w\d])esc(?![\w\d]+).*").match(context.content.lower()):
        await context.channel.send(f"ESC BAD PunOko")

    if re.compile(r".*(?<![\w\d])brb(?![\w\d]+).*").match(context.content.lower()):
        await context.channel.send(f"see you later, @{context.author.name}! have a good one! <3 <3 <3 <3")

    if ("sup vladisbot" in context.content.lower()) or ("sup chat" in context.content.lower()):
        await context.channel.send(f"nm, just vibin peepoComfy")

    if any(re.compile(f".*(?<![\w\d]){i}(?![\w\d]+).*").match(context.content.lower()) is not None for i in ['rip', 'oof', 'f']):
        await context.channel.send("oh no PepeHands")
        pass 

    if any(i in context.content.lower() for i in ["bye chat", "bye vladisbot"]):
        await context.channel.send(f"Farewell @{context.author.name}, take care of yourself and have a great one! <3 <3 <3 <3 ")

    # if 'hello' in ctx.content.lower():
    #         await ctx.channel.send(f"Hi, @{ctx.author.name}!")
    # .*(?<!\w)[f,oof,rip](?![\w,\d]+).*
if __name__ == "__main__":
    bot.run()
    pass