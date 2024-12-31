import pytest
from django.urls import reverse
from news.models import News

@pytest.mark.django_db
def test_news_list_view(client):
    News.objects.create(title="Finance News", content="Content", category="finance")
    url = reverse("news_list")
    response = client.get(url, {"category": "finance"})
    assert response.status_code == 200
    assert "Finance News" in response.content.decode()
