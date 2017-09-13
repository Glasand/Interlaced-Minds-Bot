import pytz
import datetime


def GetTime(timezone):
    a = datetime.datetime.now() # UTC
    b = datetime.datetime.now(tz=pytz.timezone(timezone)) # for Japan time zone
    return b.strftime("%H:%M:%S") #formatting