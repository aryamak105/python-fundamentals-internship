import requests
import streamlit as st

api = "853cb43f03b4ca25a4549663755d6d44"

st.title("Weather App")

city = st.text_input("Enter City Name")

if st.button("Search"):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        st.subheader("City : " + data["name"])
        st.write("Temperature :", data["main"]["temp"], "°C")
        st.write("Weather :", data["weather"][0]["main"])
        st.write("Description :", data["weather"][0]["description"])
        st.write("Humidity :", data["main"]["humidity"], "%")
        st.write("Wind Speed :", data["wind"]["speed"], "m/s")

    else:
        st.error("City not found")