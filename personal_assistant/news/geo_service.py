import requests


class GeoService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/geo/1.0/zip"

    def get_coordinates_by_zip(self, zip_code, country_code="US"):
        try:
            params = {
                "zip": f"{zip_code},{country_code}",
                "appid": self.api_key,
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()  # Возвращает координаты (lat, lon)
        except requests.RequestException as e:
            print(f"Ошибка запроса: {e}")
            return {"error": str(e)}