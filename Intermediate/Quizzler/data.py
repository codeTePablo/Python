import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}  #  we use parameters to create 10 new questions each time

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  #  Check HTTP Status Codes
data = response.json()  #  return json data
question_data = data["results"]
