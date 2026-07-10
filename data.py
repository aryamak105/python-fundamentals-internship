import requests
import json

response = requests.get("https://fakestoreapi.com/products")
data = response.json()

print("Title is : ",data[0][ 'title'])
print("Title is : ",data[1][ 'title'])
print("Title is : ",data[3][ 'title'])
print("Title is : ",data[4][ 'title'])


print("Price is : ",data[0][ 'price'])
print("Price is : ",data[1][ 'price'])
print("Price is : ",data[2][ 'price'])
print("Price is : ",data[3][ 'price'])