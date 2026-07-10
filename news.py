import requests
import streamlit as st

url = "https://newsdata.io/api/1/latest?apikey=pub_51a8a036f53b45548d3122a9ddafc25b&country=in&language=en"

response = requests.get(url)
data = response.json()

st.title("Latest News")

for news in data["results"]:
    st.subheader(news["title"])
    st.write(news["description"])
    st.write(news["link"])
    st.write("--------------------------------")
   
    