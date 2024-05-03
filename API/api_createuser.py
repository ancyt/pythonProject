import requests
import json

# json_file=open("users.json")
# json_payload=json.load(json_file)
#
# resp=requests.post("https://reqres.in/api/users",data=json_payload)

json_data=open("users.json","r").read()
resp=requests.post("https://reqres.in/api/users",data=json.loads(json_data))
print(resp.status_code)
print(resp.json())
print(resp.headers.get('content-type'))
assert resp.json()["job"]=="tester1"