import discord
import asyncio
from discord.ext import commands
import botobject
import time
import getTime

bot = botobject.bot
GMT = ["BhunaBoy", "BenTechy66", "Oliverh57", "Dylan The Spud"]
BOT = ["Interlaced Minds Official Bot", "BenBot"]
GER = ["Mr. SoUndso"] #
POL = ["Lolex"]

async def GetTime(username):
    username = username[:-5]
    if username in GMT:
        return getTime.GetTime("Europe/London")
    elif username in BOT:
        return "BOT"
    elif username in GER:
        return getTime.GetTime("Europe/Berlin")
    elif username in GER:
        return getTime.GetTime("Europe/Warsaw")
        
    else:
        return "??:??"