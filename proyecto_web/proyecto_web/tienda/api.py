from urllib.request import urlopen
import json

url = "https://random-data-api.com/api/commerce/random_commerce?size=100"

response = urlopen(url)
data = json.load(response)
diccionario = {}
j = 0
for i in data:
    if i ["material"] not in diccionario.values():
        diccionario[j]=i["material"]
        j +=1
print(diccionario.values())