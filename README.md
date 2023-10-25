# OpenWeatherMap API Python Script README

## Overview

This Python script allows you to fetch and display weather information for a specified city using the OpenWeatherMap API. It prompts you to enter the name of a city, sends a request to the API, and displays the weather description and temperature in Celsius.

## Prerequisites

Before using this script, make sure you have the following prerequisites:

- Python: You need to have Python installed on your computer. You can download it from [Python's official website](https://www.python.org/downloads/).
- The `requests` library: You can install it using `pip` by running the command `pip install requests`.

## Usage

1. **API Key Configuration:**

   You will need to sign up on the [OpenWeatherMap website](https://openweathermap.org/) to obtain an API key. Once you have the API key, replace `"**************"` in the script with your API key:

   ```python
   API_KEY = "your_api_key_here"
   ```

2. **Run the Script:**

   To use the script, simply run it from your terminal or code editor. You will be prompted to enter the name of the city for which you want to fetch weather information:

   ```python
   python weather_info.py
   ```

3. **View Weather Information:**

   The script will send a request to the OpenWeatherMap API with the provided city name and your API key. If the request is successful (status code 200), it will display the following information:

   - Weather description: A brief description of the weather conditions in the specified city.
   - Temperature: The temperature in Celsius.

   If there is an error, it will display an "An error occurred" message.

## Data Storage

The script does not store any data locally. It sends a request to the OpenWeatherMap API in real-time and displays the response.

## Author

This weather information script was created by Aranya Dutta. If you have any questions or need further assistance, please feel free to contact me at [thisisaro.official@gmail.com].

## License

Working on it

---

