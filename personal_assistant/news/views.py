from django.shortcuts import render
from personal_assistant.news.services import NewsService


# Используйте свой API-ключ
NEWS_API_KEY = "ваш_api_ключ"


def news_list(request):
    category = request.GET.get("category")
    service = NewsService(api_key=NEWS_API_KEY)
    news = service.fetch_news(category=category)
    context = {
        "news": news,
        "category": category,
    }
    return render(request, "news/news_list.html", context)


def news_sources(request):
    service = NewsService(api_key=NEWS_API_KEY)
    sources = service.fetch_sources()
    context = {"sources": sources}
    return render(request, "news/news_sources.html", context)
