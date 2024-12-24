import requests

class CurrencyServic:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def fetch_rates(self):
        response = requests.get(f"{self.api_url}?apikey={self.api_key}")
        response.raise_for_status()
        return response.json().get("rates", {})
