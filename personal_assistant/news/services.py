import requests


class NewsService:
    def __init__(self, api_key, base_url="https://newsapi.org/v2"):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_news(self, category=None, country="us", page_size=10):
        url = f"{self.base_url}/top-headlines"
        params = {
            "apiKey": self.api_key,
            "country": country,
            "pageSize": page_size,
        }
        if category:
            params["category"] = category

        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("articles", [])
        else:
            return []

    def fetch_sources(self):
        url = f"{self.base_url}/sources"
        params = {"apiKey": self.api_key}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("sources", [])
        else:
            return [
                {"name": "Source 1", "description": "Description 1"},
                {"name": "Source 2", "description": "Description 2"},
            ]
