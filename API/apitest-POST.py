import requests
head={
    'accept':'text/plain',
    'content-type':'application/json'
}

request_payload={
  "id": 20,
  "idBook": 100,
  "firstName": "ancy",
  "lastName": "thomas"
}

response=requests.post("https://fakerestapi.azurewebsites.net/api/v1/Authors",headers=head,json=request_payload)

print(response.status_code)
data=response.json()
assert data['id']==20