import requests

# resp=requests.get("https://reqres.in/api/users?page=2")
para={
    "page":2
}
resp=requests.get("https://reqres.in/api/users",params=para)
json_data=resp.json()
assert json_data["total"]==12,"total not matching"
print (json_data["data"][0]["email"])

assert (json_data["data"][0]["email"]).endswith("reqres.in"),"email id is not correct"

print(json_data["data"][1]["first_name"])
assert (json_data["data"][1]["first_name"])!=None,"it should not be none"
