import requests
import logging

class NewsService:
    def __init__(self, api_key, base_url="https://newsapi.org/v2"):
        self.api_key = api_key
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)  # Вы можете настроить уровень логирования

    def fetch_news(self, category=None, country="us", page_size=10, language="en", from_date=None, to_date=None):
        url = f"{self.base_url}/top-headlines"
        params = {
            "apiKey": self.api_key,
            "country": country,
            "pageSize": page_size,
            "language": language,
        }

        if category:
            params["category"] = category
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            articles = response.json().get("articles", [])
            print(articles)  # Выводим статьи в консоль для проверки
            return articles
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching news: {e}")
            return []


    def fetch_sources(self):
        url = f"{self.base_url}/sources"
        params = {"apiKey": self.api_key}
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json().get("sources", [])
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching sources: {e}")
            # Можно вернуть дефолтные значения или пустой список
            return [
                {"name": "Source 1", "description": "Description 1"},
                {"name": "Source 2", "description": "Description 2"},
            ]
