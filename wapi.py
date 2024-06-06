import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

def display_weather(weather_data):
    if weather_data:
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
        
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_description}")
    else:
        print("No data to display.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "679e5bda5f2d9ad7e2d71b1398831a7c"
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)
