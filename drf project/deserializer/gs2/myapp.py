import requests
import json
URL = "http://127.0.0.1:8000/studcreate/"

data = {
    'name':'vansh',
    'roll': 65,
    'city':'u.p',
}
# data = {
#     'name':'ketan',
#     'roll':432,
#     'city':'jaspur',
# }
# data = {
#     'name':'ketan',
#     'roll':432,
#     'city':'jaspur',
# }

json_data = json.dumps(data)

r = requests.post(url = URL,data = json_data)
data = r.json
print(data)