#Import libraries
import discord #The Discord API
import asyncio #Used for await and async
from discord.ext import commands #Used to define commands and some other things

#Import other dependencies created by Ben
import credentials #The Bot's Secret Key
import online #The CheckOnlineUsers function
import botobject #The global bot object




bot = botobject.bot #import the bot object


bot.loop.create_task(online.CheckOnlineUsers()) #create coroutine

@bot.command()
async def debug():
    roles = []
    rolesname = []
    roles = bot.get_server("297674982773882892").role_hierarchy
    for role in roles:
        rolesname.append(role.name)
    rolesname.remove("@everyone")
    await bot.say(rolesname)

bot.run(credentials.BotSecret) #run bot
