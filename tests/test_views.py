"""Module providing a function printing python version."""

import pytest
from django.urls import reverse

# from news.models import News
from unittest.mock import patch
import requests


@pytest.mark.django_db
def test_new_list_view(client):
    """Function test_news_list_view printing python version."""
    url = reverse("news:news_list")
    response = client.get(url, {"category": "finance"})
    assert response.status_code == 200
    assert "Финансы" in response.content.decode()


@pytest.mark.django_db
def test_news_list_view(client):
    """Function test_news_list_view printing python version."""
    response = client.get(reverse("news:news_list"))
    assert response.status_code == 200
    assert "categories" in response.context


@pytest.mark.django_db
@patch("news.views.NewsService.fetch_news")
def test_ne_list_view(mock_fetch_news, client):
    mock_fetch_news.return_value = [
        {
            "title": "Test News",
            "description": "Test Content",
            "category": "finance",
            "url": "",
            "image_url": "",
        }
    ]

    url = reverse("news:news_list")
    response = client.get(url)

    assert response.status_code == 200
    assert "Test News" in response.content.decode("utf-8")


# @pytest.mark.django_db
# @patch("news.views.NewsService.fetch_news")
# def test_ne_list_category_filter(mock_fetch_news, client):
#     mock_fetch_news.return_value = [
#         {"title": "Finance News", "description": "Content", "category": "finance", "url": "", "image_url": ""},
#         {"title": "Sports News", "description": "Content", "category": "sports", "url": "", "image_url": ""},
#     ]

#     url = reverse("news:news_list")
#     response = client.get(url, {"category": "finance"})

#     assert response.status_code == 200
#     content = response.content.decode("utf-8")
#     assert "Finance News" in content
#     assert "Sports News" not in content


@pytest.mark.django_db
@patch('news.services.NewsService.fetch_news')
def test_ne_list_category_filter(mock_fetch_news, client):
    """Test filtering by category in news list."""
    
    # Настройка мока
    mock_fetch_news.return_value = [
        {"title": "Finance News", "content": "Content", "category": "finance"},
    ]
    
    # Запрос
    url = reverse("news:news_list")
    response = client.get(url, {"category": "finance"})
    
    # Проверки
    assert response.status_code == 200
    content = response.content.decode("utf-8")
    assert "Finance News" in content  # Должно быть



@pytest.mark.django_db
@patch('news.services.NewsService.fetch_news')
def test_n_list_category_filter(mock_fetch_news, client):
    """Test filtering by category in news list."""
    
    # Настройка мока
    mock_fetch_news.return_value = [
        {"title": "Finance News", "content": "Content", "category": "finance"},
    ]
    
    # Запрос
    url = reverse("news:news_list")
    response = client.get(url, {"category": "finance"})
    
    # Проверки
    assert response.status_code == 200
    content = response.content.decode("utf-8")
    assert "Finance News" in content  # Должно быть

