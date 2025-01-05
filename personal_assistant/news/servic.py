"""Module providing a function printing python version."""

import requests

class CurrencyServic:
    """Class CurrencyServic representing a person"""
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def fetch_rates(self):
        """Function fetch_rates printing python version."""
        response = requests.get(f"{self.api_url}?apikey={self.api_key}", timeout=10)
        response.raise_for_status()
        return response.json().get("rates", {})
# Этот код не рабочий