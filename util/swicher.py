from aero.intro import *

def epi():
    token = input(f"{lr} Account Token {b}> {lr} ")

    while True:
        setting = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch('https://discord.com/api/v7/users/@me/settings', headers={'Authorization': token}, json=setting)
