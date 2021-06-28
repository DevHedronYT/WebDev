import requests, random, string

## POST Request
pUrl = "http://127.0.0.1:5000/user"

rString = ''.join(random.choice(string.ascii_letters) for _ in range(10))
user = { 
        "name"    : rString, 
        "email"   : rString + "@gmail.com",  
        "address" : rString + "addr",
        "phone"   : str(random.randint(0, 10000000000)),
}

pRequest = requests.post(pUrl, json = user)
print(pRequest.text)

## GET Request
gUrl = "http://127.0.0.1:5000/user/descending_id"

gRequest = requests.get(gUrl)
print(gRequest.text)

