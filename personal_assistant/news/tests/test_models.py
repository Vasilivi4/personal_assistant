import pytest
from news.models import News

@pytest.mark.django_db
def test_news_model():
    news = News.objects.create(title="Test Title", content="Test Content", category="finance")
    assert news.title == "Test Title"
    assert news.content == "Test Content"
    assert news.category == "finance"
