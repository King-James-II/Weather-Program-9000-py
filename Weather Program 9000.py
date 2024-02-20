# This program prompts the user to enter a city name or zip code and
# uses a request to pull the data from an online API as a JSON file
# stores the data in a library and then pull the data needed to show
# the user a formatted weather forecast. 
# importing JSON and requests modules to handle JSON data and requests
# from online API.
import json
import requests

# this method prints weather information for the city entered from the JSON
# dictionary that was received from the API request.
def print_weather(city, weather_info):
    print (f"\nConnection Successful.\n\nDisplaying weather for:")
    if city.isdigit():
        print(f"{weather_info['name']}, {weather_info['sys']['country']}, {city}")
    else:
        print(f"{weather_info['name']}, {weather_info['sys']['country']}")
    print("-------------------------------------------------------")
    print(f"{round(weather_info['main']['temp'])}°F")
    print(f"Status: {weather_info['weather'][0]['main']}")
    print(f"Description: {weather_info['weather'][0]['description'].title()}")
    print(f"Feels like: {round(weather_info['main']['feels_like'])}°F")
    print(f"Humidity: {weather_info['main']['humidity']}%")
    print(f"Wind: {round(weather_info['wind']['speed'])} mph")

# method that will print an error message if the data is unable to be received 
# from the API and displays a proper message to whether it was the connection
# or if the user may have entered a zip code or city that couldn't be found.
def error_msg(city, error_code):
    if error_code == 404:
        print(f'\nConnection Sucessful.\nUnable to find zip code or city: "{city}".')
    else:
        print("Unable to establish a connection.\nCheck your internet connection")
    error_code = 0

# main method that calls all of the methods to perform the program's functions.
def main():
    print("Welcome to weather program 9000\n--------------------------------")
    print("Powered by: OpenWeather.org")
    continue_running = "yes"
    request_weather(continue_running)

# method that loops while the user selects to continue looking up weather data
# and takes the city name or zipcode from the user and sends a request using
# the city name or zipcode to the API to retrieve the weather data and calls 
# either an error message or prints the weather to the console. 
def request_weather(continue_running):
    error_code = 0
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    appid = "79be24a786b43ae656b247883c9b8aab"
    while continue_running == 'yes':

        city = input("Please input your city name / zipcode:")
        if city.isdigit():
            url =f"{base_url}?zip={city},us&appid={appid}&units=imperial"

#  Try block to catch exceptions and display messages for both connection issues
#  as well ass if the server is unable to find the zip code or city requested
#  by the user.
            try:
                response = requests.get(url)
                weather_info = response.json()
                error_code = response.status_code
                weather_info['name']

            except:
                error_msg(city, error_code)

            else:
                print_weather(city, weather_info)

        elif type(city) == str:
            url =f"{base_url}?q={city},us&appid={appid}&units=imperial"

            try:
                response = requests.get(url)
                weather_info = response.json()
                error_code = response.status_code
                weather_info['name']

            except:
                error_msg(city, error_code)

            else:
                print_weather(city, weather_info)

        else:
            print ("Invalid input please input a correct value.")
            continue

# loop to determine whether or not the program continues to run or not.
        while continue_running == 'yes':
            continue_running = input("would you like to check the forecast again? (yes/no)").lower()

            if continue_running == 'no':
                break
            elif continue_running == 'yes':
                break
            else:
                print("Invalid response please enter again.")
                continue_running = 'yes'
                continue
main()