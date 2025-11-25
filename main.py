import requests 

api_key = "b3b58d3427ba0fac3eff1de660b7c94f"

MY_LAT = 43.464951
MY_LONG = -80.523911

response = requests.get(url = f"https.//api.openweathermap.org/data/2.5/forecast?lat={MY_LAT}&lon={MY_LONG}&appid={api_key}")
response.raise_for_status()
print(response)