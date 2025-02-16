from aero.intro import *

def close_all_dms(token):
    headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
    for channel in close_dm_request:
        print(f"ID: "+channel['id'])
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}", headers=headers,)
