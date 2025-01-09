"""Module providing a function printing python version."""

import os
import requests
from django.shortcuts import render
from django.conf import settings
from dotenv import load_dotenv
from newsapi import NewsApiClient
from news.models import News
from news.services import NewsService
from news.weather_service import WeatherAPI

load_dotenv(dotenv_path=".env")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def news_list(request):
    """Function news_list printing python version."""
    categories = [
        {"key": "finance", "name": "Finance", "api_category": "business"},
        {"key": "sports", "name": "Sports", "api_category": "sports"},
        {"key": "technology", "name": "Technology", "api_category": "technology"},
        {"key": "health", "name": "Health", "api_category": "health"},
        {"key": "entertainment", "name": "Entertainment", "api_category": "entertainment"},
    ]

    selected_category = request.GET.get("category")
    category_mapping = {cat["key"]: cat["api_category"] for cat in categories}
    api_category = category_mapping.get(selected_category)

    if News.objects.exists():
        if selected_category:
            news = News.objects.filter(category=selected_category)
        else:
            news = News.objects.all()
    else:
        service = NewsService(api_key=settings.NEWS_API_KEY)
        if api_category:
            news = service.fetch_news(category=api_category)
        else:
            news = service.fetch_news()

    context = {
        "news": news,
        "categories": categories,
        "selected_category": selected_category,
    }

    return render(request, "news/news_list.html", context)

def news_sources(request):
    """Function news_sources printing python version."""
    service = NewsService(api_key=NEWS_API_KEY)
    sources = service.fetch_sources()

    context = {
        "sources": sources,
    }
    return render(request, "news/news_sources.html", context)

def get_top_headlines():
    """Function get_top_headlines printing python version."""
    return newsapi.get_top_headlines(
        q="bitcoin",
        sources="bbc-news,the-verge",
        category="business",
        language="en",
        country="us",
    )

def get_all_articles():
    """Function get_all_articles printing python version."""
    return newsapi.get_everything(
        q="bitcoin",
        sources="bbc-news,the-verge",
        domains="bbc.co.uk,techcrunch.com",
        from_param="2017-12-01",
        to="2017-12-12",
        language="en",
        sort_by="relevancy",
        page=2,
    )

def get_sources():
    """Function get_sources printing python version."""
    return newsapi.get_sources()

def news_view(request):
    """Function news_view printing python version."""
    api_key = settings.NEWS_API_KEY
    news_service = NewsService(api_key=api_key)

    news = news_service.fetch_news()

    return render(request, "news/news_list.html", {"news": news})

def weather_widget_view(request):
    """Function weather_widget_view."""
    city = request.GET.get("city", "Kyiv")
    weather_api = WeatherAPI(settings.WEATHER_API_KEY)
    weather_data = weather_api.get_current_weather(city)

    return render(
        request,
        "news/weather_widget.html",
        {"weather_data": weather_data, "city": city},
    )

def fetch_rates(self):
    """Function fetch_rates printing python version."""
    try:
        response = requests.get(self.api_url)
        response.raise_for_status()
        data = response.json()

        rates = data.get('rates', {})

        usd_to_eur = rates.get('EUR', 'Not available')
        usd_to_gbp = rates.get('GBP', 'Not available')

        return {
            'USD to EUR': usd_to_eur,
            'USD to GBP': usd_to_gbp,
        }

    except requests.exceptions.RequestException as e:
        return {'error': f"Error fetching data: {e}"}

def contact_us(request):
    """Function contact_us printing python version."""
    return render(request, "news/contact_link.html")

def terms_and_conditions(request):
    """Function terms_and_conditions printing python version."""
    return render(request, "news/terms_link.html")

def index(request):
    """Function index printing python version."""
    city = "Kyiv"
    weather_api = WeatherAPI(settings.WEATHER_API_KEY)
    weather_data = weather_api.get_current_weather(city)

    context = {
        "city": city,
        "weather_data": weather_data,
    }
    return render(request, "index.html", context)

def fetch_news(self, category=None):
    """Function fetch_news printing python version."""
    try:
        response = newsapi.get_top_headlines(
            category=category,
            language="en",
            country="us",
        )
        return response.get("articles", [])
    except Exception as e:
        return {"error": str(e)}
