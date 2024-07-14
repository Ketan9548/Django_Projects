import json
import requests

URL = "http://127.0.0.1:8000/studentapi/"

# for get method
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL,data=json_data)
    data = r.json()
    print(data)

# get_data(1)


#for post method
def post_data():
    data = {
        'name':'sumit',
        'roll': 121,
        'city':'noida',
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL,data=json_data)
    data = r.json()
    print(data)

# post_data()

# for update
def updete_data():
    data = {
        'id':6,
        'name':'harsh',
        'roll': 873,
        'city':'jaspur',
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL,data=json_data)
    data = r.json()
    # print(data)


# updete_data()

# for delete
def delete_data():
    data = {
        'id':2,
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL,data=json_data)
    data = r.json()
    print(data)

# delete_data()
