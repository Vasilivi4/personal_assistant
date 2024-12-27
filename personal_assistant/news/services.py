from django.shortcuts import render
import requests
import logging
from news.models import NewsSummary
from django import forms

class CategoryForm(forms.Form):
    CATEGORY_CHOICES = [
        ('business', 'Business'),
        ('entertainment', 'Entertainment'),
        ('general', 'General'),
        ('health', 'Health'),
        ('science', 'Science'),
        ('sports', 'Sports'),
        ('technology', 'Technology'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False, label="Category")

class NewsService:
    def __init__(self, api_key, base_url="https://newsapi.org/v2"):
        self.api_key = api_key
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)

    def fetch_news(self, category=None, country="us", page_size=15, language="en", from_date=None, to_date=None, user=None):
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

            # Сохраняем новости в базу данных
            for article in articles:
                NewsSummary.objects.create(
                    user=user,  # Указываем текущего пользователя
                    title=article['title'],
                    content=article.get('description', ''),
                    date=article['publishedAt'][:10]  # Публикационная дата, обрезаем до даты (без времени)
                )

            return articles
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching news: {e}")
            return []


    def fetch_sources(self):
        url = f"{self.base_url}/sources"
        params = {"apiKey": self.api_key}
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json().get("sources", [])
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching sources: {e}")
            return [
                {"name": "Source 1", "description": "Description 1"},
                {"name": "Source 2", "description": "Description 2"},
            ]

def news_list_view(request):
    form = CategoryForm(request.GET)  # Получаем данные формы из GET-запроса
    news = []

    if form.is_valid():
        selected_category = form.cleaned_data.get('category')
        if selected_category:
            news_service = NewsService(api_key='your_api_key')
            news = news_service.fetch_news(category=selected_category)  # Получаем новости по выбранной категории
    else:
        # Если форма не отправлена, получаем все новости
        news = NewsSummary.objects.all().order_by('-date')  # Получаем все новости, отсортированные по дате

    return render(request, 'news/news_list.html', {'news': news, 'form': form})

