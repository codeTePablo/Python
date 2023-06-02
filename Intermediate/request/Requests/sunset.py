import requests
from datetime import datetime

lat = 19.432608
lon = -99.133209

parameters = {"lat": lat, "lng": lon, "formatted": 0}

mexico_city = "https://api.sunrise-sunset.org/json?lat=19.432608&lng=-99.133209"  #  Have lat and lng
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = (
    data["results"]["sunrise"].split("T")[1].split(":")[0]
)  #  Amanecer, ['2023-01-27', '13:11:13+00:00'], hour (['13', '11', '13+00', '00'])
print(sunrise)

time_now = datetime.now()

print(time_now.hour)
