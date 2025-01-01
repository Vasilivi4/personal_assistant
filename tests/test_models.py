import pytest
from django.contrib.auth.models import User
from news.models import NewsSummary, News


@pytest.mark.django_db(transaction=True)
def test_news_model():
    news = News.objects.create(title="Test Title", content="Test Content", category="finance")
    assert news.title == "Test Title"
    assert news.content == "Test Content"
    assert news.category == "finance"


@pytest.mark.django_db
def test_news_summary_model():
    # Создаем пользователя
    user = User.objects.create(username="testuser")
    
    # Создаем экземпляр модели NewsSummary
    news_summary = NewsSummary.objects.create(
        user=user,
        title="Summary Title",
        content="Summary Content",
    )
    
    # Проверяем поля
    assert news_summary.title == "Summary Title"
    assert news_summary.content == "Summary Content"
    assert news_summary.user == user

    # Проверяем строковое представление
    assert str(news_summary) == "Summary Title"

@pytest.mark.django_db
def test_news_model_invalid_category():
    with pytest.raises(ValueError):
        News.objects.create(title="Invalid Category", content="Test Content", category="invalid")

@pytest.mark.django_db
def test_news_model_blank_content():
    news = News.objects.create(title="Test Title", content="", category="sports")
    assert news.content == ""

@pytest.mark.django_db
def test_news_filter_by_category():
    News.objects.create(title="Finance News", content="Finance Content", category="finance")
    News.objects.create(title="Sports News", content="Sports Content", category="sports")

    # Фильтрация по категории
    finance_news = News.objects.filter(category="finance")
    assert len(finance_news) == 1
    assert finance_news[0].title == "Finance News"

    sports_news = News.objects.filter(category="sports")
    assert len(sports_news) == 1
    assert sports_news[0].title == "Sports News"
