from aero.intro import *

def change_status(token, status):
    url = "https://discord.com/api/v10/users/@me/settings"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "status": "online",  # You can set this to "idle", "dnd", or "invisible"
        "activity": {
            "name": status,
            "type": 0  # 0 = Playing, 1 = Streaming, 2 = Listening, 3 = Watching
        }
    }

    response = requests.patch(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print(" Status changed successfully!")
    else:
        print(f" Failed to change status: {response.status_code} - {response.text}")

