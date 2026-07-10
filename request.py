import requests
import json

response = requests.get("https://fakestoreapi.com/products")
data = response.json()

with open("product.json", "w") as file:
    json.dump(data,file)

print("Data stored successfully!!")    