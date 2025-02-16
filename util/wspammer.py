from aero.intro import *

def wspam():
    hook = input(f"{lr} Webhook {b}> {lr}")
    msg = input(f"{lr} Message {b}> {lr}")
    amount = (int(input(f"{lr} Amount {b}> {lr}")))

    for i in range(amount):
        requests.post(hook, data={"content": f"{msg}"})
        print(fade.pinkred("Sent > {msg}"))
    input(f"{lr} Press ENTER to continue > ")