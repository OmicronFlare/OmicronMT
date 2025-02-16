from aero.intro import *


def get_account_info(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    
    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        print(" Username:", user_data['username'])
        print(" User  ID:", user_data['id'])
        print(" Email:", user_data.get('email', 'Email not available'))
        print(" Phone Number:", user_data.get('phone', 'Phone number not available'))
    else:
        print("Failed to retrieve account information. Status code:", response.status_code)
