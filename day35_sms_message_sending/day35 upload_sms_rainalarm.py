import requests
import os
from twillo.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("api_key")
account_sid = os.environ.get("acct_sid")
auth_token = os.environ.get("auth_token")

#city_name = "Chicago"

weather_params = {
    "lat":41.85 ,
    "lon":-87.65,
    "appid":api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#http://jsonviewer.stack.hu/
#print(response.json())
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body= "It's going to rain today! As always,trust the process, young king 👑",
        from_="+19853337728",
        to= "# the phone number you want to send to",
    )
    print(message.status)