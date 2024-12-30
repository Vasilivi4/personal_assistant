"""Module providing a function printing python version."""

import logging
import requests
from django.shortcuts import render
from django import forms
from news.models import NewsSummary


class CategoryForm(forms.Form):
    """Class CategoryForm representing a person"""

    CATEGORY_CHOICES = [
        ("business", "Business"),
        ("entertainment", "Entertainment"),
        ("general", "General"),
        ("health", "Health"),
        ("science", "Science"),
        ("sports", "Sports"),
        ("technology", "Technology"),
    ]
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES, required=False, label="Category"
    )


class NewsService:
    """Class NewsService representing a person"""

    def __init__(self, api_key, base_url="https://newsapi.org/v2"):
        self.api_key = api_key
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)

    def fetch_news(
        self,
        category=None,
        country="us",
        page_size=15,
        language="en",
        from_date=None,
        to_date=None,
        user=None,
    ):
        """Function fetch_news printing python version."""
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
            response.raise_for_status()
            articles = response.json().get("articles", [])

            for article in articles:
                NewsSummary.objects.create(
                    user=user,
                    title=article["title"],
                    content=article.get("description", ""),
                    date=article["publishedAt"][:10],
                )

            return articles
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching news: {e}")
            return []

    def fetch_sources(self):
        """Function fetch_sources printing python version."""
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
    """Function news_list_view printing python version."""
    form = CategoryForm(request.GET)
    news = []

    if form.is_valid():
        selected_category = form.cleaned_data.get("category")
        if selected_category:
            news_service = NewsService(api_key="your_api_key")
            news = news_service.fetch_news(category=selected_category)
    else:

        news = NewsSummary.objects.all().order_by("-date")

    return render(request, "news/news_list.html", {"news": news, "form": form})
