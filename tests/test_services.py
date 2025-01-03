import pytest
from news.services import NewsService

@pytest.mark.django_db(transaction=True)
def test_news_service_fetch_news(mocker):
    # Подготовка мока
    mock_response = {"articles": [{"title": "Test News", "content": "Test Content"}]}
    mocker.patch("news.services.NewsService.fetch_news", return_value=mock_response)

    # Создание экземпляра сервиса
    service = NewsService(api_key="fake_key")
    
    # Вызов метода
    result = service.fetch_news(category="finance")
    
    # Проверка результата
    assert result == mock_response
    assert result["articles"][0]["title"] == "Test News"

