"""Module providing a function printing python version."""

import requests

class WeatherAPI:
    """Class WeatherAPI representing a person"""
    def __init__(self, api_key):
        self.base_url = "http://api.weatherapi.com/v1"
        self.api_key = api_key

    def get_current_weather(self, city, lang="ru"):
        """Function create_contact printing python version."""
        endpoint = f"{self.base_url}/current.json"
        params = {
            "key": self.api_key,
            "q": city,
            "lang": lang
        }

        try:
            response = requests.get(endpoint, params=params, timeout=10)# Дабавил timeout=10
            response.raise_for_status()
            data = response.json()

            location = data.get('location', {})
            current = data.get('current', {})
            
            return {
                "location": location.get('name', 'Неизвестно'),
                "region": location.get('region', 'Неизвестно'),
                "country": location.get('country', 'Неизвестно'),
                "temperature": current.get('temp_c', 'Нет данных'),
                "condition": current.get('condition', {}).get('text', 'Нет данных'),
                "wind_speed": current.get('wind_kph', 'Нет данных'),
                "humidity": current.get('humidity', 'Нет данных'),
                "local_time": location.get('localtime', 'Нет данных')
            }

        except requests.exceptions.RequestException as e:
            return {"error": f"Ошибка при запросе: {e}"}
