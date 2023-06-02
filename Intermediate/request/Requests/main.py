import requests

# response = requests.get(
#     url="http://api.open-notify.org/iss-now.json"
# )  #  Api to give some iss position (aero spacial base)
# response.raise_for_status()  #  Check HTTP Status Codes
# data = response.json()  #  return json data
# # print(data)  #  {'timestamp': 1674779390, 'iss_position': {'latitude': '-49.4497', 'longitude': '62.0073'}, 'message': 'success'}
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)  #  Tuple
# print(iss_position)

response = requests.get("https://api.kanye.rest/")
quote = response.json()
print(quote["quote"])
