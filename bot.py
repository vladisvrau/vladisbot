from twitchio.ext import commands
import os
from discord import DISCORD_DIC
import re
import random
import json

bot = commands.Bot(
    # set up the bot
    token=os.environ['TMI_TOKEN'],
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.command(name='test')
async def test(context):
    await context.send("First Try!")

@bot.command(name='race')
async def race(context):
    with open("runners.json") as _file: 
        runners = json.load(_file)
        message = " | ".join([f"{i}" for i in runners if i.lower() != str(context.channel).lower()])
        _multitwitch = "/".join(runners)
        multitwitch = f"https://multitwitch.tv/{_multitwitch}"
        join_us_ = "You're welcome to join us in CBF's discord: https://discord.com/invite/nU9fN6Z"
        final = f"We're doing races to encourage no-resets and getting used to running against other people. I'm running with {message} . Watch us on multitwitch: {multitwitch} .  {join_us_}"
        await context.send(final)

@bot.command(name='yolo')
async def yolo(context):
    with open("runners.json") as _file: 
        final = f"I'm yoloing a category and that means that I have a rough understanding of how the route goes and literally no knowledge about the tricks used. It's fun, I promise."
        await context.send(final)

    
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

# @bot.command(name='so')
# async def shout_out(context):
#     shout_out = context.content.split("!so")[-1].strip()
#     shout_out = shout_out.replace("@", "")
#     # print(context.content)
#     await context.send(f"Checkout {shout_out} at twitch.com/{shout_out}")
#     pass

@bot.command(name='husbando')
async def husbando(context):
    await context.send("Berry's Husbando is Daruk's descendant, Yunobo. Kappa")
    pass

# @bot.command(name='discord')
# async def discord(context):
#     discord_link = DISCORD_DIC.get(str(context.channel), None)
#     if discord_link is not None:
#         await context.send(f"Join the Discord: {discord_link}")
#     else:
#         await context.send("Sorry, I couldn't find the discord link for this channel ¯\_(ツ)_/¯")
#     pass

@bot.command(name='partytime')
async def partytime(context):
    await context.send("pepeD let's pepeD party pepeD people pepeD")


@bot.command(name='arrest')
async def arrest(context):
    prisoner = context.content.split("!arrest")[-1].strip()
    await context.send(f"STOP! YOU'VE VIOLATED THE LAW! PAY THE COURT A FINE OR SERVE YOUR SENTENCE! YOUR STOLEN GOODS ARE NOW FORFEIT, {prisoner.upper()}!")
    pass

@bot.command(name='bonk')
async def bonk(context):
    prisoner = context.content.split("!bonk")[-1].strip()
    await context.send(f"{prisoner} has been bonked")
    pass

# @bot.command(name='love')
# async def love(context):
#     await context.send(f"alexan90Heart alexan90Heart alexan90Heart alexan90Heart alexan90Heart alexan90Heart alexan90Heart")
#     pass

@bot.command(name='prayer')
async def love(context):
    await context.send(f"Dear RNGeezus, please bless Link's belly with bananas and keep our quivers full of arrows. Please temper the bokos to work with us, not against us. Keep our beetles on our trees and deliver us from the evil of Ganon going to the wall. Hell yeah.")
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

    if 'Wanna become famous? Buy followers, primes and views on bigfollows*com (bigfollows . com)!'.lower() in context.content.lower():
        await context.channel.ban(context.author.name) 

    greets = [
        "hello vladisbot",
        "hi vladisbot",
        "hello chat",
        "hi chat",
        "hey vladisbot",
        "hey @vladisbot",
        "hello @vladisbot",
        "hi @vladisbot",
        "hey chat"
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

    if any(i in context.content.lower() for i in ["thank you vladisbot", "thanks vladisbot", "Cheers, mate!"]):
        options = ["np homie", "you're very welcome", "don't mention it", "you're welcome", "I didnt do it for you."]
        await context.channel.send(options[random.randint(0, len(options)-1)])

    # if 'hello' in ctx.content.lower():
    #         await ctx.channel.send(f"Hi, @{ctx.author.name}!")
    # .*(?<!\w)[f,oof,rip](?![\w,\d]+).*
if __name__ == "__main__":
    bot.run()
    pass