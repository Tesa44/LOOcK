from threading import Timer
from config import SHELLY_URL
import requests

url = f"http://{SHELLY_URL}/rpc"

def unlockLock():
    #wczesniej trzeba tez jakos polaczyc kompa i shelly do tego samego wifi
    body = {
       "id": 0,
       "src":"tesa",
       "method":"Switch.Set",
       "params": {
         "id":1,
         "on": "true"
       }
    }

    #przyklad
    #url = 'https://jsonplaceholder.typicode.com/todos/1'
    #res = requests.get(url)
    #print(res.json())

    response = requests.post(url, json = body)

    if(response):
        #send post to turn off, or maybe its even unnecessary, because it does it automatically (I mean lock)
        #or maybe be have to send lock immidiately bcs our lock cannot stand longer ON status?
        r = Timer(10.0, lockLock)
        r.start()

        return True

    return False

def lockLock():
    body = {
        "id": 0,
        "src": "xmavv",
        "method": "Switch.Set",
        "params": {
            "id": 1,
            "on": "false"
        }
    }

    response = requests.post(url, json=body)
