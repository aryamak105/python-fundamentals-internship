import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="Currency Converter", page_icon="💰")

st.title("💰 Currency Converter")
st.write("Convert currencies using live exchange rates.")

# Currency List
currencies = [
    "USD", "INR", "EUR", "GBP", "JPY",
    "AUD", "CAD", "CHF", "CNY", "AED"
]

# Inputs
amount = st.number_input("Enter Amount", min_value=0.01, value=1.0)

from_currency = st.selectbox("From Currency", currencies)

to_currency = st.selectbox("To Currency", currencies)

# Your API Key
API_KEY = "YOUR_API_KEY"

if st.button("Convert"):

    url = f"https://v6.exchangerate-api.com/v6/{"36fff2a799c6988d3a88908d"}/latest/{from_currency}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["result"] == "success":

            rate = data["conversion_rates"][to_currency]
            converted_amount = amount * rate

            st.success(
                f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
            )

            st.info(
                f"Exchange Rate: 1 {from_currency} = {rate:.4f} {to_currency}"
            )

        else:
            st.error("API Error")
            st.write(data)

    except Exception as e:
        st.error(f"Error: {e}")