from django.shortcuts import render
import requests
from news.services import NewsService
from newsapi import NewsApiClient
from news.weather_service import WeatherAPI
from django.conf import settings

from django.conf import settings
from dotenv import load_dotenv
import os

from news.servic import CurrencyServic


load_dotenv(dotenv_path=".env")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key=NEWS_API_KEY)



def news_list(request):

    category = request.GET.get("category")


    service = NewsService(api_key=settings.NEWS_API_KEY)
    news = service.fetch_news(category=category)


    city = "Киев"
    weather_api = WeatherAPI(settings.WEATHER_API_KEY)
    weather_data = weather_api.get_current_weather(city)


    categories = [
        {"key": "finance", "name": "Финансы"},
        {"key": "sports", "name": "Спорт"},
        {"key": "technology", "name": "Технологии"},
        {"key": "health", "name": "Здоровье"},
        {"key": "entertainment", "name": "Развлечения"},
    ]

    context = {
        "news": news,
        "category": category,
        "categories": categories,
        "selected_category": category,
        "city": city,
        "weather_data": weather_data,
    }

    return render(request, "news/news_list.html", context)



def news_sources(request):

    service = NewsService(api_key=NEWS_API_KEY)
    sources = service.fetch_sources()

    city = "Киев"
    weather_api = WeatherAPI(settings.WEATHER_API_KEY)
    weather_data = weather_api.get_current_weather(city)

    context = {
        "sources": sources,
        "city": city,
        "weather_data": weather_data,
    }
    return render(request, "news/news_sources.html", context)


def get_top_headlines():
    return newsapi.get_top_headlines(
        q="bitcoin",
        sources="bbc-news,the-verge",
        category="business",
        language="en",
        country="us",
    )


def get_all_articles():
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
    return newsapi.get_sources()


def news_view(request):

    api_key = settings.NEWS_API_KEY
    news_service = NewsService(api_key=api_key)

    news = news_service.fetch_news()

    return render(request, "news/news_list.html", {"news": news})


def weather_widget_view(request):
    city = request.GET.get("city", "Киев")
    weather_api = WeatherAPI(settings.WEATHER_API_KEY)
    weather_data = weather_api.get_current_weather(city)

    return render(
        request,
        "news/weather_widget.html",
        {"weather_data": weather_data, "city": city},
    )

def daily_summary(request):

    currency_service = CurrencyServic(api_url=f"https://openexchangerates.org/api/latest.json?app_id={settings.CURRENCY_API_KEY}")
    rates = currency_service.fetch_rates()

    context = {
        "rates": rates,
    }

    return render(request, "news/daily_summary.html", context)

def fetch_rates(self):
    try:
        response = requests.get(self.api_url)
        response.raise_for_status()
        data = response.json()


        rates = data.get('rates', {})

        usd_to_eur = rates.get('EUR', 'Не доступно')
        usd_to_gbp = rates.get('GBP', 'Не доступно')

        return {
            'USD to EUR': usd_to_eur,
            'USD to GBP': usd_to_gbp,
        }

    except requests.exceptions.RequestException as e:
        return {'error': f"Ошибка при получении данных: {e}"}

def contact_us(request):
    return render(request, "news/contact_link.html")

def terms_and_conditions(request):
    return render(request, "news/terms_link.html")