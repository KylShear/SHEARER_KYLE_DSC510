import requests

api_key = "6f09e938dd576d719c79519e0476c28e"


# Function to convert temperature from Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


# Function to convert temperature from Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


# Function to print weather data in a formatted manner
def print_weather_data(weather_data, temperature_unit):
    temperature_converter = kelvin_to_celsius if temperature_unit.lower() == 'c' else kelvin_to_fahrenheit

    # Print a separator line for better readability
    print("\n-------------------------------------------------------")
    print("-------------------------------------------------------\n")

    # Print weather details
    print("Weather in {}: ".format(weather_data['name']))
    print("-------------------------------------------------------")
    print(
        "Temperature: {:.2f} {}".format(temperature_converter(weather_data['main']['temp']), temperature_unit.upper()))
    print("Feels like: {:.2f} {}".format(temperature_converter(weather_data['main']['feels_like']),
                                         temperature_unit.upper()))
    print("Min Temperature: {:.2f} {}".format(temperature_converter(weather_data['main']['temp_min']),
                                              temperature_unit.upper()))
    print("Max Temperature: {:.2f} {}".format(temperature_converter(weather_data['main']['temp_max']),
                                              temperature_unit.upper()))
    print("Pressure: {} hPa".format(weather_data['main']['pressure']))
    print("Humidity: {}%".format(weather_data['main']['humidity']))
    print("Wind Speed: {:.2f} m/s".format(weather_data['wind']['speed']))
    print("Description: {}".format(weather_data['weather'][0]['description']))
    print("Cloudiness: {}%".format(weather_data['clouds']['all']))
    print("Visibility: {} meters".format(weather_data['visibility']))
    print("Sunrise: {}".format(weather_data['sys']['sunrise']))
    print("Sunset: {}".format(weather_data['sys']['sunset']))

    # Print another separator line for better readability
    print("\n-------------------------------------------------------")
    print("-------------------------------------------------------")
    print("-------------------------------------------------------\n")


# Function to get weather forecast by city name
def get_weather_forecast_by_city(city_name):
    if city_name.isdigit() or len(city_name) <= 2:
        print("Invalid city name. Please enter a valid City name.")
        return None
    # Get location details using the OpenWeatherMap Geo API
    weather_loc = requests.get(
        url="http://api.openweathermap.org/geo/1.0/direct?q={}&limit=5&appid={}".format(city_name, api_key))
    try:
        # Extract latitude and longitude from the location data
        lat = weather_loc.json()[0]["lat"]
        lon = weather_loc.json()[0]["lon"]

        # Get weather data using the OpenWeatherMap Weather API
        weather_data = requests.get(
            url="http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&limit=5&appid={}".format(lat, lon, api_key))

        return weather_data.json()
    except:
        print("Invalid Input")
        return None


# Function to get weather forecast by ZIP code
def get_weather_forecast_by_zip(zip_code):
    if not zip_code.isdigit() or len(zip_code) != 5:
        print("Invalid ZIP Code. Please enter a valid 5-digit ZIP Code.")
        return None
    # Get location details using the OpenWeatherMap Geo API
    weather_loc = requests.get(
        url="http://api.openweathermap.org/geo/1.0/zip?zip={}&appid={}".format(zip_code, api_key))
    try:
        # Extract latitude and longitude from the location data
        lat = weather_loc.json()["lat"]
        lon = weather_loc.json()["lon"]

        # Get weather data using the OpenWeatherMap Weather API
        weather_data = requests.get(
            url="http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&limit=5&appid={}".format(lat, lon, api_key))

        return weather_data.json()
    except:
        print("Invalid Input")
        return None

# Main function to handle user input and interaction
def main():
    print("Welcome!")

    while True:
        print("Choose from the following options: ")
        print("1. Search by Zip Code")
        print("2. Search by City")
        print("3. Quit")
        user_choice = input("Enter Choice: ")

        if user_choice == "1":
            zip_code = input("Enter Zip Code: ")
            data = get_weather_forecast_by_zip(zip_code)
            if data == None:
                continue
            temperature_unit = input("Enter Temperature Unit: (C or F)")

            # Validate user input for temperature unit
            if temperature_unit.lower() == "c" or temperature_unit.lower() == "f":
                print_weather_data(data, temperature_unit.lower())
            else:
                print("Wrong Temperature Format. Showing in the default format (Fahrenheit).")
                print_weather_data(data, "f")

        elif user_choice == "2":
            city_name = input("Enter City: ")
            data = get_weather_forecast_by_city(city_name)
            if data == None:
                continue
            temperature_unit = input("Enter Temperature Unit: (C or F)")

            # Validate user input for temperature unit
            if temperature_unit.lower() == "c" or temperature_unit.lower() == "f":
                print_weather_data(data, temperature_unit.lower())
            else:
                print("Wrong Temperature Format. Showing in the default format (Fahrenheit).")
                print_weather_data(data, "f")

        elif user_choice == "3":
            break
        else:
            print("Invalid Input\n")


if __name__ == "__main__":
    main()
