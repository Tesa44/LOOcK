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
         "id":0,
         "on": True
       }
    }

    request = {
       "id": 0,
       "src":"tesa",
       "method":"Switch.GetConfig",
       "params": {
         "id":0,
       }
    }

    #przyklad
    #url = 'https://jsonplaceholder.typicode.com/todos/1'
    #res = requests.get(url)
    #print(res.json())

    response = requests.post(url, json = body)

    # response_config = requests.post(url, json = request)
    print(response.json())
    # print(response_config)

    if(response.json()):
        #send post to turn off, or maybe its even unnecessary, because it does it automatically (I mean lock)
        #or maybe be have to send lock immidiately bcs our lock cannot stand longer ON status?
        r = Timer(3.0, lockLock)
        r.start()

        return True

    return False

def lockLock():
    body = {
        "id": 0,
        "src": "xmavv",
        "method": "Switch.Set",
        "params": {
            "id": 0,
            "on": False
        }
    }

    response = requests.post(url, json=body)

start = input()
if start == "start":
    unlockLock()


