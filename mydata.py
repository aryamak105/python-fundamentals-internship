import requests

mydata = requests.get("https://fakestoreapi.com/products")

jsondata = mydata.json()

for i in jsondata:
    print("Product :" + i['title'])