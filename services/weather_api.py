import requests
from config import OPENWEATHER_API_KEY

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=ru"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        name = data.get("name", "Неизвестно")
        temp = int(data["main"]["temp"])
        description = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return f"""
🌤 Погода в городе: {name}
🌡 Температура: {temp}°C
🌈 Описание: {description}
💧 Влажность: {humidity}%
🌬 Скорость ветра: {wind_speed} м/с
"""
    except requests.RequestException:
        return "❌ Ошибка при запросе к API погоды."
    except (KeyError, IndexError):
        return f"❌ Погода для города '{city}' не найдена."