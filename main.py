import html
import json
import requests
import os
from twilio.rest import Client


# from pip._internal.cli import status_codes

MY_LAT = 48.577950
MY_LONG = 39.306412
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
# api_key = "ede37dbf6c614d549f7f56ad6d6834e7"
api_key = os.environ["OWM_API_KEY"]




weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella",
        to="whatsapp:+84354049518"
    )
    print(message.status)
