

import json
import socket
from enum import Enum

from aiohttp import web

import Protocol

from util import dp

db = None
loop = None

async def hello(request):
  return web.Response(text="Hello World!")

async def handle(request):
  d = await request.json()
  default = web.Response()
  dp("Got request: " + str(d))
  try:
    rt = RequestType(d['type'])
  except:
    dp("Missing query type")
    return default
  if rt == RequestType.ECHO:
    a = {}
  elif rt == RequestType.LIST:
    a = dict(db.dump_map())
  elif rt == RequestType.RECENT:
    if not 'id' in d:
      db("Missing 'id' parameter")
      return default
    if not 'count' in d:
      count = 10
    else:
      count = d['count']
    a = list(db.dump_recent(d['id'], count))
    for i in range(len(a)):
      a[i] = list(a[i])
    for item in a:
      item[4] = item[4].decode('utf-8')
  elif rt == RequestType.LEDPUB:
    a = db.dump_map()
    tip = d['target']
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind(("0.0.0.0", 5155))
    sock.sendto(bytearray([0, 3, 0, 3, 0, 1] + [0 for _ in range(63)]), (tip, 5155))
    a = {}
  else:
    a = "Unknown RequestType"
  return web.Response(text=json.dumps(a))

rest_app = web.Application()
rest_app.router.add_get('/', hello)
resource = rest_app.router.add_resource('/json')
resource.add_route('*', handle)

def build_app(adb, aloop):
  global db
  global loop
  db = adb
  loop = aloop
  return rest_app

class RequestType(Enum):
  """Request body should include field 'type': 0/1/2... and any other parameters

  >>> import urllib.request
  >>> from time import sleep
  >>> import json
  >>> import os
  >>> g = os.system("python3 server.py > /dev/null &")
  >>> sleep(3)
  >>> response = urllib.request.urlopen("http://127.0.0.1:8080")
  >>> "Hello World!" == response.read().decode('UTF-8')
  True
  >>> response = urllib.request.urlopen("http://127.0.0.1:8080/json", data='{"type": 0}'.encode('UTF-8'))
  >>> len(json.loads(response.read().decode('UTF-8'))) == 0
  True
  >>> g = os.system("fuser -k 8080/tcp")

  """
  ECHO = 0 #Responds with empty JSON
  LIST = 1 #Dictionary of {'id': 'ip_addr'} pairs
  RECENT = 2 #Include 'count' field in query, default 10. Needs 'id' field. Returns msg_dict JSON array
  LEDPUB = 3
