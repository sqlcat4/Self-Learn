from locale import format_string
import requests

API_KEY="84d9e42ef52368504d80708c71bf45ff"
BASE_URL="http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a City Name")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code ==200: 
    data =response.json()
    weather=data['weather'][0]['description']

    print(weather)
    temperature=round(data["main"]["temp"]-273.15,2)
    print(temperature)

    print("weather :", weather)
    print("Temperature:", temperature, " Celcius")
else :
        print("An error occured")