"""Module providing a function printing python version."""

import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_news_list_view(client):
    """Function test_news_list_view printing python version."""
    url = reverse("news:news_list")
    response = client.get(url, {"category": "finance"})
    assert response.status_code == 200
    assert "Финансы" in response.content.decode()

