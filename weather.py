import requests
# import json

API_KEY = "a458d08cc1562491902140366bb5ffad"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)
print(response)


if response.status_code == 200:
    data = response.json()
    # with open("data.json", "w") as f:
    #     json.dump(data, f)
    weather = data['weather'][0]['description']
    print("Weather: ",weather)
    temperature = round(data['main']['temp'] - 273,2)
    print("Temperature: ",temperature," C")


else:
    print("An error occured.")
