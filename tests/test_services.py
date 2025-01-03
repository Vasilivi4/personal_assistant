"""Module providing a function printing python version."""

import pytest
from news.services import NewsService
from news.weather_service import WeatherAPI

@pytest.mark.django_db(transaction=True)
def test_news_service_fetch_news(mocker):
    """Function test_news_service_fetch_news printing python version."""
    mock_response = {"articles": [{"title": "Test News", "content": "Test Content"}]}
    mocker.patch("news.services.NewsService.fetch_news", return_value=mock_response)

    service = NewsService(api_key="fake_key")
    
    result = service.fetch_news(category="finance")
    
    assert result == mock_response
    assert result["articles"][0]["title"] == "Test News"

@pytest.fixture
def mock_weather_service():
    return WeatherAPI(api_key="fake_key")

def test_weather_service_get_current_weather(mocker, mock_weather_service):
    # Мок-ответ от API
    mock_response = {
        "location": {
            "name": "Киев",
            "region": "Киевская область",
            "country": "Украина",
            "localtime": "2025-01-01 12:00"
        },
        "current": {
            "temp_c": 5,
            "condition": {"text": "Облачно"},
            "wind_kph": 15,
            "humidity": 80
        }
    }

    # Замена requests.get
    mock_requests_get = mocker.patch("requests.get")
    mock_requests_get.return_value = mocker.Mock(
        status_code=200,
        json=lambda: mock_response,
        raise_for_status=lambda: None
    )

    # Вызов метода
    result = mock_weather_service.get_current_weather("Киев")

    # Проверки
    assert result["location"] == "Киев"
    assert result["region"] == "Киевская область"
    assert result["country"] == "Украина"
    assert result["temperature"] == 5
    assert result["condition"] == "Облачно"
    assert result["wind_speed"] == 15
    assert result["humidity"] == 80
    assert result["local_time"] == "2025-01-01 12:00"
