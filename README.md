# Weather Program 9000
## Weather Forecast Application

This application fetches weather data from an online API based on the user's input of a city name or zip code. It then presents the weather forecast in a formatted manner to the user.

## Key Features:
- **API Integration**: Utilizes the OpenWeatherMap API to fetch weather data.
- **User Input Handling**: Accepts input of city name or zip code from the user.
- **JSON Parsing**: Parses the JSON response received from the API to extract relevant weather information.
- **Error Handling**: Displays appropriate error messages if the connection fails or if the entered city or zip code is not found.
- **Formatted Weather Display**: Presents the weather forecast including temperature, weather status, description, feels-like temperature, humidity, and wind speed in a user-friendly format.

## Technologies and Concepts Covered:
- **API Requests**: Utilizes the `requests` module to send HTTP requests to the OpenWeatherMap API.
- **JSON Parsing**: Uses the `json` module to parse the JSON response received from the API.
- **Error Handling**: Implements try-except blocks to catch and handle exceptions such as connection errors or invalid responses.
- **User Input Handling**: Accepts user input through the command line and validates it before making API requests.
- **Data Formatting**: Formats the weather forecast data for easy readability using string formatting techniques.
- **Looping**: Utilizes loops to repeatedly prompt the user for input and continue fetching weather data until the user decides to stop.

