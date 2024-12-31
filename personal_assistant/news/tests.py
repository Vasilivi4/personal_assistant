import pytest
from django.urls import reverse
from news.models import News

@pytest.mark.django_db
def test_news_list_view(client):
    # Создаем тестовые данные
    News.objects.create(title="Test News", content="Test Content", category="finance")

    # Делаем запрос к представлению
    url = reverse("news_list")  # Убедитесь, что имя маршрута соответствует вашему
    response = client.get(url)

    # Проверяем, что страница загружается
    assert response.status_code == 200
    assert "Test News" in response.content.decode()

@pytest.mark.django_db
def test_news_list_category_filter(client):
    # Создаем тестовые данные
    News.objects.create(title="Finance News", content="Content", category="finance")
    News.objects.create(title="Sports News", content="Content", category="sports")

    # Фильтруем по категории
    url = reverse("news_list")
    response = client.get(url, {"category": "finance"})

    # Проверяем, что фильтр работает
    assert response.status_code == 200
    assert "Finance News" in response.content.decode()
    assert "Sports News" not in response.content.decode()
