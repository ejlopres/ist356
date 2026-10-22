import requests
uri = "https://portal.app.cent-su.org/api/funnyname/random?n=5"
response = requests.get(uri)
#deserialize the reponse to a python object
response.raise_for_status()
data = response.json()
for name in data:
    print(name['first'], name['last'])


# print(data)
# print(type(data))
# first_person = data[0]
# print(first_person['first'], first_person['last'])


#convert the below to python code
uri = "https://portal.app.cent-su.org/api/weather/geocode?language=en&count=2&place=Syracuse%2C%20New%20York"
headers = {
    "accept": "application/json",
    "X-API-KEY": "442642d6e78691cc4a23727a"
}
response = requests.get(uri, headers=headers)
response.raise_for_status()
data = response.json()
print(data)

data = response.json()
df = pd.json_normalize(data['results'])
print(df)