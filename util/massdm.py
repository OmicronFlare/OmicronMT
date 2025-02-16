from aero.intro import *

def girona():
    token = input(f"{lr} Account Token {b}> {lr}")
    msg = input(f"{lr} Message {b}> ")

    rs = requests.Session()
    headers = {"Authorization": token, "User -Agent": "Mozilla/5.0"}

    # Retrieve the list of DM channels
    response = rs.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve channels. Status code: {response.status_code}")
        print("Response:", response.text)
        return

    channels = response.json()
    print(f" Retrieved {len(channels)} DM channels.")  # Debugging output

    for channel in channels:
        # Check if the channel is a DM channel
        if channel['type'] == 1:  # DM channel type is 1
            json_data = {"content": msg}
            t.sleep(1)  # Sleep for 1 second between messages
            response = rs.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers=headers, json=json_data)
            
            if response.status_code == 200:
                print(f"Message sent to channel ID: {channel['id']}")
            else:
                print(f"Failed to send message to channel ID: {channel['id']}. Status code: {response.status_code}. Response: {response.text}")