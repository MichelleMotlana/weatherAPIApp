import requests
#API KEY
API_KEY = "adef718bdb6c4c51a2081309252702"  
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city):
    params = {"key": API_KEY, "q": city, "aqi": "no"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        weather = {
            "City": data["location"]["name"],
            "Country": data["location"]["country"],
            "Temperature": f"{data['current']['temp_c']}°C",
            "Humidity": f"{data['current']['humidity']}%",
            "Condition": data["current"]["condition"]["text"]
        }
        return weather
    else:
        return f"Error: {data.get('error', {}).get('message', 'Unknown error')}"

# User input
city = input("Enter name of your city: ")
#Get weather for entered location
weather_data = get_weather(city)

# Display results
if isinstance(weather_data, dict):
    for key, value in weather_data.items():
        print(f"{key}: {value}")
else:
    print(weather_data)

