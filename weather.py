import requests
import json
class weather:
    def __init__(self, city, temp):
        self.temp = temp
        self.city = city

    @staticmethod
    def get_temp(city):
        api_key = "03f6dbab56f5bd99b44fa7117d790ea8"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"{city.title()} is currently at {temp}°C with {desc}"
        else:
            return f"Invalid city or something went wrong"
