import requests
url = "https://www.fcswap.com/game/pokemon-go"
data = {"code": 573167543491, "codetext": 573167543491}

requests.post(url, data)