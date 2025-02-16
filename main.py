from aero.intro import *
from util.tokgrabber import *
from util.wspammer import *
from util.wdeleter import *
from util.snuker import *
from util.swicher import *
from util.massdm import *
from util.infono import *
from util.status import *
from util.closedm import *


invite = f" {lr}https://discord.gg/RDQ78h5D6a"

def creditz():
    print(fade.pinkred(f" -  omicron.nn In Discord\n -  Vision \n - {invite}"))
    Write.Input(f" Press [ENTER] to return > ", Colors.red_to_purple)

Anime.Fade(Center.Center(intrologo), Colors.red_to_black, Colorate.Vertical, interval=0.035, enter=True)

secondmainlogo = """



   ____            _                     
  / __ \____ ___  (_)_____________  ____ 
 / / / / __ `__ \/ / ___/ ___/ __ \/ __ \ 
/ /_/ / / / / / / / /__/ /  / /_/ / / / /
\____/_/ /_/ /_/_/\___/_/   \____/_/ /_/ 

"""
print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))

def ice():
    conel = Write.Input(f" <@omicron.event> ► ", Colors.purple_to_red)
    if conel == "1":
        clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))
        grabbing()

    if conel == "2":
        clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))
        wspam()

    if conel == "3":
        clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))
        wdel()

    if conel == "4":
        clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))
        spinner()

    if conel == "5":
        clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))
        creditz()

    if conel == "10":
        print(invite)
        webbrowser.open("https://discord.gg/RDQ78h5D6a")
        rtn = input(f"{lr} Press ENTER to return {b}> ")

    if conel == "11":
        clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))
        token = input(f" {lr}Account Token {b}> {lr}")
        get_account_info(token)
        rtn = input(f"{lr} Press ENTER to return {b}> ")

    if conel == "12":
        clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))
        epi()

    if conel == "13":
        clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))
        girona()
        rtn = input(f"{lr} Press ENTER to return {b}> ")

    if conel == "14":
        clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))
        token = input(f" {lr}Token {b}> ")
        status = input(f" {lr}Status {b}> {lr} ")
        change_status(token, status)
        rtn = input(f"{lr} Press ENTER to return {b}> ")
    
    if conel == "15":
        clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))
        token = input(f" {lr}Token {b}> ")
        close_all_dms(token)
        rtn = input(f"{lr} Press ENTER to return {b}> ")

    if conel == "a":
        clear()
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))
            

while True:
    clear()
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(secondmainlogo)))
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(selection)))
    ice()