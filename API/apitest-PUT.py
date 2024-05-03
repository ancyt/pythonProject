import requests

head_GET={
    'Accept':'text/plain',
    'content-type':'application/json'
}

response_GET=requests.get("https://fakerestapi.azurewebsites.net/api/v1/Authors/12",headers=head_GET)

print("before update")
print(response_GET.json())

head_PUT={
    'Accept':'text/plain',
    'content-type':'application/json'
}
payload_PUT={'id': 12,
             'idBook': 4,
             'firstName': 'Ancy',
             'lastName': 'Thomas'}

response_PUT=requests.put("https://fakerestapi.azurewebsites.net/api/v1/Authors/12",headers=head_PUT,json=payload_PUT)
print("After Update")
print(response_PUT.json())