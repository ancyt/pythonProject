import requests

base_url='https://gorest.co.in/public/v2/users'

para={
    'page':1,
    'per_page':2
}

response=requests.get(url=base_url,params=para)
print(response.json())