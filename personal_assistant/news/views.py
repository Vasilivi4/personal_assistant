from django.shortcuts import render
from news.services import NewsService
from newsapi import NewsApiClient

# Используйте свой API-ключ
NEWS_API_KEY = "76f31ecb7a7a44b18ea3acb372a988c3"

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
