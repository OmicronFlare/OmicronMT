import colorama
import pystyle
import os
import subprocess as s
import fade
import asyncio
import webbrowser
import random
import requests
import json
import re
import time as t
import discord
from discord.ext import commands
import uuid
import ctypes
import shutil
from colorama import *
from colorama import Fore
from pystyle import *
from urllib.request import Request, urlopen

def set_console_title(title: str):
   ctypes.windll.kernel32.SetConsoleTitleW(title)

def clear():
    os.system("cls" if os.name=="nt" else "clear")   

set_console_title("[+] Omicron Multi Tool - BETA")  

w = Fore.WHITE
r = Fore.RED
b = Fore.LIGHTBLACK_EX
g = Fore.LIGHTGREEN_EX
c = Fore.CYAN
m = Fore.LIGHTMAGENTA_EX
ll = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
fr = Fore.RESET
ly = Fore.LIGHTYELLOW_EX

intrologo = """
    ___            _                     
  / __ \____ ___  (_)_____________  ____ 
 / / / / __ `__ \/ / ___/ ___/ __ \/ __ \ 
/ /_/ / / / / / / / /__/ /  / /_/ / / / /       By Omicron [Press ENTER]
\____/_/ /_/ /_/_/\___/_/   \____/_/ /_/ 

"""
## Upper for anime fade

selection = """

                                    
01 > Token Grabber          06 > Token Lookup          11 > Account Information
02 > Webhook Spammer        07 > Server Lookup         12 > Glitch
03 > Webhook Deleter        08 > Nitro Generator       13 > Mass DM
04 > Server Nuker           09 > CC Generator          14 > Status Changer
05 > Credits                10 > Discord               15 > DM Deleter
                                

"""

## second upper for menu

mainlogo = """

   ____            _                     
  / __ \____ ___  (_)_____________  ____ 
 / / / / __ `__ \/ / ___/ ___/ __ \/ __ \ 
/ /_/ / / / / / / / /__/ /  / /_/ / / / /
\____/_/ /_/ /_/_/\___/_/   \____/_/ /_/ 
                                        
"""
## third upper for main logo/title


nukebot = """

01 > Delete Channels  |  [-ext]
O2 > Create Channels  |  [-create <amount> <name>]
03 > Create Roles     |  [-croles <amount> <name>]
04 > Delete Roles     |  [-droles]
05 > Kick Everyone    |  [-kickall]
06 > Spam Messages    |  [-spam <message> <amount>]
07 > Exterminator     |  [-nuke <channel name> <message>]

    
"""
