"""Module providing a function printing python version."""

import pytest
from django.urls import reverse
from news.models import News

@pytest.mark.django_db
def test_news_list_view(client):
    News.objects.create(title="Test News", content="Test Content", category="finance")

    url = reverse("news:news_list")
    response = client.get(url)

    assert response.status_code == 200
    assert "Test News" in response.content.decode()

@pytest.mark.django_db
def test_news_list_category_filter(client):
    News.objects.create(title="Finance News", content="Content", category="finance")
    News.objects.create(title="Sports News", content="Content", category="sports")

    url = reverse("news:news_list")
    response = client.get(url, {"category": "finance"})

    assert response.status_code == 200
    assert "Finance News" in response.content.decode()
    assert "Sports News" not in response.content.decode()
