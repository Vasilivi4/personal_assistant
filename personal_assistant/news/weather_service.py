"""Module providing a function printing python version."""

import requests

class WeatherAPI:
    """Class WeatherAPI representing weather information."""

    def __init__(self, api_key):
        self.base_url = "http://api.weatherapi.com/v1"
        self.api_key = api_key

    def get_current_weather(self, city, lang="en"):
        """Function get_current_weather printing python version."""
        endpoint = f"{self.base_url}/current.json"
        params = {
            "key": self.api_key,
            "q": city,
            "lang": lang
        }

        try:
            response = requests.get(endpoint, params=params, timeout=10)  # Added timeout=10
            response.raise_for_status()
            data = response.json()

            location = data.get('location', {})
            current = data.get('current', {})

            return {
                "location": location.get('name', 'Unknown'),
                "region": location.get('region', 'Unknown'),
                "country": location.get('country', 'Unknown'),
                "temperature": current.get('temp_c', 'No data'),
                "condition": current.get('condition', {}).get('text', 'No data'),
                "wind_speed": current.get('wind_kph', 'No data'),
                "humidity": current.get('humidity', 'No data'),
                "local_time": location.get('localtime', 'No data')
            }

        except requests.exceptions.RequestException as e:
            return {"error": f"Error during request: {e}"}
