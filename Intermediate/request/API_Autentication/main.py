import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "92dffdfbae650e6d0e2c5828e6016ac7"

account_sid = "AC89ce1f24a0e5677d00168acad43a39b7"
auth_token = "b21d28baa24cc86587aee06e1f3ed582"

MY_LAT = "19.432608"
MY_LON = "-99.133209"

# api_key = os.environ.get("OWM_API_KEY")
# account_sid = "YOUR ACCOUNT SID"
# auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key
    # "units": "metric"
    # "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

weather_slice = weather_data["weather"][0]["description"]
print(weather_slice)

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Това е предупредително съобщение за акаунта j**04@gmail.com I SEE YOU, https://onx.la/6d269.",
    from_="+19893598175",
    to="+527294460095",
)
print(message.status)
