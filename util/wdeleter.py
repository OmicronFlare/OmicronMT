from aero.intro import *

def wdel():
    hook = input(f"{lr} Webhook {b}> {lr}")
    msg = input(f"{lr} Deletion Message {b}> {lr}")
    requests.post(hook, data={"content": f"{msg}"})
    requests.delete(hook)