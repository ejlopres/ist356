import requests
import streamlit as st

st.title("Weather App")

def geocode(place:str) -> (float,float)
uri = "https://portal.app.cent-su.org/api/weather/geocode?language=en&count=2&place=Syracuse%2C%20New%20York"
headers = {
    "accept": "application/json",
    "X-API-KEY": "442642d6e78691cc4a23727a"
}
response = requests.get(uri, headers=headers)
response.raise_for_status()
data = response.json()
print(data)