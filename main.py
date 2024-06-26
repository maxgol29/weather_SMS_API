import requests
from twilio.rest import Client
import os

API_KEY = os.environ.get("OWM_API_KEY")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


LATITUDE = 26.671799
LONGITUDE = 80.976563
weather_params = {
    "lon": LONGITUDE,
    "lat": LATITUDE,
    "appid": API_KEY,
    "cnt": 4
}


OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for weather in weather_data["list"]:
    if weather["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Today is going a rain",
        from_="+18557290537",
        to="+12103885318",
    )
    print(message.status)