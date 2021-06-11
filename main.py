import requests

URL = "https://corona.lmao.ninja/v2/countries/THA"
read = requests.get(url = URL)
data = read.json()

for i in data : 
    print(i, "->", data[i])

