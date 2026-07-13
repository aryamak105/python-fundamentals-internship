import requests
import streamlit as st

mydata = requests.get("https://fakestoreapi.com/products")

mydata1 = mydata.json()

for i in mydata1:
    st.title(i['title'])
    st.subheader(i['price'])
    st.image(i['image'])
    
