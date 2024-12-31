import pytest
from news.services import NewsService

@pytest.mark.django_db
def test_news_service_fetch_news(mocker):
    mock_response = {"articles": [{"title": "Test News", "content": "Test Content"}]}
    mocker.patch("news.services.NewsService.fetch_news", return_value=mock_response)

    service = NewsService(api_key="fake_key")
    result = service.fetch_news(category="finance")
    assert result["articles"][0]["title"] == "Test News"
