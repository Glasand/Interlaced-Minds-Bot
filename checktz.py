import discord
import asyncio
from discord.ext import commands
import botobject
import time
import getTime

bot = botobject.bot
GMT = ["BhunaBoy", "BenTechy66", "Oliverh57", "Dylan The Spud", "Geenium"]
BOT = ["Interlaced Minds Official Bot", "BenBot"]
GER = ["Mr. SoUndso", "CommandLord aka illio"]
POL = ["Lolex"]
LOS = ["BluePsychoRanger"]
EST = ["Rai-Eclipse13", "GuineaNumber2", "GuineaPvP", "Landmine752"]
JER = ["Simple Rick"]
MAD = ["TheRahn"]

async def GetTime(username):
    username = username[:-5]
    if username in GMT:
        return getTime.GetTime("Europe/London")
    elif username in BOT:
        return "BOT"
    elif username in GER:
        return getTime.GetTime("Europe/Berlin")
    elif username in POL:
        return getTime.GetTime("Europe/Warsaw")
    elif username in LOS:
        return getTime.GetTime("America/Los_Angeles")
    elif username in EST:
        return getTime.GetTime("EST")
    elif username in JER:
        return getTime.GetTime("Asia/Jerusalem")
    elif username in MAD:
        return getTime.GetTime("Europe/Madrid")
        
    else:
        return "??:??"