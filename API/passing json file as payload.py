import requests
import json

base_url='https://reqres.in/'

header={
    'content-type':'application/json'
}

json_file=open('./users.json')
json_payload=json.load(json_file)

response=requests.post(url=base_url+'api/users',headers=header,json=json_payload)
print(response.status_code)
print(response.text)