import discord
import asyncio
from discord.ext import commands
import botobject
import time
import getTime

bot = botobject.bot
GMT = ["BhunaBoy", "BenTechy66"]
BOT = ["Interlaced Minds Official Bot", "BenBot"]

async def GetTime(username):
    username = username[:-5]
    if username in GMT:
        #return time.strftime("%H:%M:%S" ,getTime.GetTime("Europe/London"))
        return getTime.GetTime("Europe/London")
        #return "GMT"
    elif username in BOT:
        return "BOT"
        
    else:
        return "??:??"