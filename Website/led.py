try:
  import requests
except ImportError:
  raise SystemExit("Error! You are missing the 'requests' library. Please install using the pip3 utility.")

#Configuration
server = "http://172.20.10.4:5154/"

def led_example():
  r = requests.post(server + "json", data='{"type": 3, "target": "172.20.10.4"}'.encode('utf-8'))
  #LED turned on!

led_example()