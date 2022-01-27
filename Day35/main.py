import requests
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACa1b3d20a72e67f4f45e5d956e14c5443"
auth_token = os.environ.get("OWN_AUTH_TOKEN")
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWN_API_KEY")

parameters = {
    "lat": 56.511311,
    "lon": 21.011190,
    "appid": api_key,
    "exclude":"current,minute,daily"
}

response = requests.get(url = OWN_Endpoint, params = parameters)
#"https://api.openweathermap.org/data/2.5/onecall?lat=50.737431&lon=7.098207&exclude=current,minutely,daily,alerts&appid=69f04e4613056b159c2761a9d9e664d2")
#print(response.status_code)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Bring an umberella ☔️",
                     from_='+17753837116',
                     to='+4915782219700'
                 )
    print(message.status)




