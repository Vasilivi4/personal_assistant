"""Module providing a function printing python version."""

import pytest
from unittest.mock import patch
from django.urls import reverse
import requests
from news.models import News
from news.views import fetch_rates, get_all_articles, get_top_headlines


@pytest.mark.django_db
def test_new_list_view(client):
    """Function test_new_list_view printing python version."""
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
    """Function test_ne_list_view printing python version."""
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


@pytest.mark.django_db
@patch("news.views.NewsService.fetch_news")
def test_ne_list_category_filter(mock_fetch_news, client):
    mock_fetch_news.return_value = [
        {"title": "Finance News", "description": "Content", "category": "finance", "url": "", "image_url": ""},

    ]

    url = reverse("news:news_list")
    response = client.get(url, {"category": "finance"})

    assert response.status_code == 200
    content = response.content.decode("utf-8")
    assert "Finance News" in content



@pytest.mark.django_db
@patch('news.services.NewsService.fetch_news')
def test_net_list_category_filter(mock_fetch_news, client):
    """Function test_ne_list_category_filter printing python version."""
    
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
    """Function test_n_list_category_filter printing python version."""
    
    mock_fetch_news.return_value = [
        {"title": "Finance News", "content": "Content", "category": "finance"},
    ]
    
    url = reverse("news:news_list")
    response = client.get(url, {"category": "finance"})
    
    assert response.status_code == 200
    content = response.content.decode("utf-8")
    assert "Finance News" in content

@pytest.mark.django_db
def test_news_list_with_category(client):
    """Function test_news_list_with_category printing python version."""
    News.objects.create(title="Sports", content="Content", category="sports")
    
    response = client.get('', {'category': 'finance'})
    assert response.status_code == 200
    content = response.content.decode('utf-8')
    assert "Sports" not in content


def test_news_sources(client, mocker):
    """Function test_news_sources printing python version."""
    mock_fetch_sources = mocker.patch('news.services.NewsService.fetch_sources')
    mock_fetch_sources.return_value = [
        {'id': 'bbc-news', 'name': 'BBC News'},
        {'id': 'cnn', 'name': 'CNN'}
    ]
    
    response = client.get('/news/sources/')
    assert response.status_code == 200
    content = response.content.decode('utf-8')
    assert "BBC News" in content
    assert "CNN" in content

def test_weather_widget_view(client, mocker):
    """Function test_weather_widget_view printing python version."""
    mock_get_current_weather = mocker.patch('news.weather_service.WeatherAPI.get_current_weather')
    mock_get_current_weather.return_value = {
        'temperature': 20,
        'condition': 'Clear sky',
        'wind_speed': 5,
        'humidity': 80,
        'local_time': '12:00',
        'error': None
    }

    response = client.get('/weather_widget/', {'city': 'Kiev'})
    assert response.status_code == 200
    content = response.content.decode('utf-8')


    assert "Температура: 20°C" in content
    assert "Состояние: Clear sky" in content
    assert "Скорость ветра: 5 км/ч" in content
    assert "Влажность: 80%" in content
    assert "Местное время: 12:00" in content


def test_index(client):
    """Function test_index printing python version."""
    response = client.get('/')
    assert response.status_code == 200
    content = response.content.decode('utf-8')
    assert "<h1>Главная страница</h1>" in content

def test_contact_us(client):
    """Function test_contact_us printing python version."""
    response = client.get('/contact/')
    assert response.status_code == 200
    content = response.content.decode('utf-8')
    assert "<h1>Свяжитесь</h1>" in content

def test_terms_and_conditions(client):
    """Function test_terms_and_conditions printing python version."""
    response = client.get('/terms/')
    assert response.status_code == 200
    content = response.content.decode('utf-8')
    assert "<h1>Условия</h1>" in content


@patch('newsapi.NewsApiClient.get_top_headlines')
def test_get_top_headlines(mock_get_top_headlines):
    """Function test_get_top_headlines printing python version."""
    mock_get_top_headlines.return_value = {'articles': [{'title': 'Top Headline', 'content': 'Content'}]}

    result = get_top_headlines()

    print("Result from get_top_headlines:", result)

    assert isinstance(result, dict)
    articles = result.get('articles', [])
    
    assert isinstance(articles, list)
    assert len(articles) > 0
    assert articles[0]['title'] == 'Top Headline'


@patch('newsapi.NewsApiClient.get_everything')
def test_get_all_articles(mock_get_all_articles):
    """Function test_get_all_articles printing python version."""
    mock_get_all_articles.return_value = {'articles': [{'title': 'Article', 'content': 'Content'}]}

    result = get_all_articles()

    print("Result from get_all_articles:", result)

    assert isinstance(result, dict)
    articles = result.get('articles', [])
    
    assert isinstance(articles, list)
    assert len(articles) > 0
    assert articles[0]['title'] == 'Article'

