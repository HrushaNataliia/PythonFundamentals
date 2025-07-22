import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

def get_weather(city):

    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric',
            'lang': 'uk'
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            weather_data = {
                'city': data['name'],
                'status': data['weather'][0]['description'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data.get('wind', {}).get('speed', 'N/A'),
                'clouds': data['clouds']['all'],
                'temp_min': data['main']['temp_min'],
                'temp_max': data['main']['temp_max'],
                'pressure': data['main']['pressure']
            }

            return weather_data
        else:
            print(f"Помилка API: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Помилка мережі: {e}")
        return None
    except KeyError as e:
        print(f"Помилка обробки даних: {e}")
        return None
    except Exception as e:
        print(f"Загальна помилка: {e}")
        return None


def format_weather_info(weather_data):
    if not weather_data:
        return "Не вдалося отримати дані про погоду"

    info = f"Місто: {weather_data['city']}\n"
    info += f"Опис: {weather_data['status']}\n"
    info += f"Температура: {weather_data['temperature']:.1f}°C\n"
    info += f"Мін/Макс: {weather_data['temp_min']:.1f}°C / {weather_data['temp_max']:.1f}°C\n"
    info += f"Вологість: {weather_data['humidity']}%\n"
    info += f"Тиск: {weather_data['pressure']} гПа\n"
    info += f"Вітер: {weather_data['wind_speed']} м/с\n"
    info += f"Хмарність: {weather_data['clouds']}%"

    return info
