from django.shortcuts import render
from news.services import NewsService
from newsapi import NewsApiClient
from django.conf import settings
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")  # Загружаем переменные из .env

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Инициализируем объект NewsApiClient один раз
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def news_list(request):
    category = request.GET.get("category")
    
    # Используем сервис для получения новостей
    service = NewsService(api_key=NEWS_API_KEY)
    news = service.fetch_news(category=category)
    
    context = {
        "news": news,
        "category": category,
    }
    
    return render(request, "news/news_list.html", context)


def news_sources(request):
    # Используем сервис для получения источников
    service = NewsService(api_key=NEWS_API_KEY)
    sources = service.fetch_sources()
    
    context = {"sources": sources}
    return render(request, "news/news_sources.html", context)

# Функция для получения топ-новостей
def get_top_headlines():
    return newsapi.get_top_headlines(
        q='bitcoin',
        sources='bbc-news,the-verge',
        category='business',
        language='en',
        country='us'
    )

# Функция для получения всех статей
def get_all_articles():
    return newsapi.get_everything(
        q='bitcoin',
        sources='bbc-news,the-verge',
        domains='bbc.co.uk,techcrunch.com',
        from_param='2017-12-01',
        to='2017-12-12',
        language='en',
        sort_by='relevancy',
        page=2
    )

# Функция для получения источников новостей
def get_sources():
    return newsapi.get_sources()

from django.shortcuts import render
from .services import NewsService
from django.conf import settings

def news_view(request):
    # Получаем API ключ из настроек
    api_key = settings.NEWS_API_KEY
    news_service = NewsService(api_key=api_key)
    
    # Получаем новости
    news = news_service.fetch_news()

    # Передаем новости в шаблон
    return render(request, 'news/news_list.html', {'news': news})
