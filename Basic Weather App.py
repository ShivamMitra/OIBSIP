import requests

# Replace with your OpenWeatherMap API key
API_KEY = "Bd5e378503939ddaee76f12ad7a97608"

# Function to get weather data based on city name
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        # Extract relevant weather information
        main = data["main"]
        weather = data["weather"][0]["description"]
        temperature = main["temp"] - 273.15  # Convert Kelvin to Celsius

        # Format and return the weather information
        return f"In {city}, the weather is {weather} with a temperature of {temperature:.2f}°C."
    else:
        return f"Error: City not found."
# User input for city name
city = input("Enter a city name: ")

# Get and display weather information
weather_info = get_weather(city)
print(weather_info)