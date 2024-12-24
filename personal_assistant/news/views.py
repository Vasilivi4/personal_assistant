from django.shortcuts import render
from news.services import NewsService
from newsapi import NewsApiClient
from news.weather_service import WeatherAPI
from django.conf import settings

from django.conf import settings
from dotenv import load_dotenv
import os


load_dotenv(dotenv_path=".env")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key=NEWS_API_KEY)


def news_list(request):
    category = request.GET.get("category")

    # Получение новостей
    service = NewsService(api_key=settings.NEWS_API_KEY)
    news = service.fetch_news(category=category)

    # Получение погоды
    city = "Киев"  # Укажите город по умолчанию или сделайте его динамическим
    weather_api = WeatherAPI(settings.WEATHER_API_KEY)
    weather_data = weather_api.get_current_weather(city)

    context = {
        "news": news,
        "category": category,
        "city": city,
        "weather_data": weather_data,
    }

    return render(request, "news/news_list.html", context)


def news_sources(request):

    service = NewsService(api_key=NEWS_API_KEY)
    sources = service.fetch_sources()

    city = "Киев"  # Укажите город по умолчанию или сделайте его динамическим
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
    city = request.GET.get("city", "Киев")  # Город из GET-параметра, по умолчанию Киев
    weather_api = WeatherAPI(settings.WEATHER_API_KEY)
    weather_data = weather_api.get_current_weather(city)

    return render(
        request,
        "news/weather_widget.html",
        {"weather_data": weather_data, "city": city},
    )
