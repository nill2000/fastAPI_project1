import requests

apiURL = "http://127.0.0.1:8000/get-item/1"

res = requests.get(apiURL).json()

print(res["Item"]["name"])