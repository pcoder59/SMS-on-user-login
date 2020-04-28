import utmp
import requests

with open("/var/log/wtmp", "rb") as f:
    buf=f.read()
    a = utmp.read(buf)
    for entry in a:
        time = entry.time

f.close()

connected = True

while connected:
    with open("/var/log/wtmp", "rb") as f:
        buf=f.read()
        a = utmp.read(buf)
        for entry in a:
            b = entry.time
        
    if(b != time):
        print("Someone Logged in!!!")
        time = b
        resp = requests.post('https://textbelt.com/text', {
        'phone': '+918606672580',
        'message': "Someone Just Logged in!!!",
        'key': 'textbelt',
        })
        print(resp.json())
    
    f.close()