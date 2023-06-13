import requests
from twilio.rest import Client
endPoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
api_key = ""  # input api key from openweathermap.org
account_sid = "AC22208e76cf3eb13149e3f4f157a3da76"  # input account id for twilio
auth_token = ""  # input auth token from twilio

# latitude and longitude set to Downtown-Houston
weather_params = {
    "lat": 29.760799,
    "lon": -95.369507,
    "appid": api_key,
}

response = requests.get(endPoint, params=weather_params)
print(response.raise_for_status())  # check connection to api
weather_data = response.json()
weather_slice = weather_data["list"][:12]  # takes 12 hours of weather data

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int (condition_code) < 700:  # anything id less than 700 will = snow, rain, and thunderstorms
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        from_='+',  # twilio phone number
        body='Its going to rain today. Remember to bring an umbrella',
        to='+'   # user phone number
    )
    print(message.status)

# go to python anywhere, set it to run at a certain time, and it'll send a text saying if it'll rain in the assigned
# area at that time that's set to run on python anywhere.
