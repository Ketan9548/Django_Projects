import requests
import json

URL1 = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'kapil',
    'roll': 981,
    'city': 'jaspur'
}

json_data = json.dumps(data)

r = requests.post(url=URL1, json=json_data)

response_data = r.json()

print(response_data)
