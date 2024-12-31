"""Module providing a function printing python version."""

from django.urls import path
from news import views


app_name = "news"

urlpatterns = [
    # path("", views.news_list, name="news_list"),
    # path("news/", views.news_list, name="news_list"),  # страница с новостями
    # path(
    #     "news/sources/", views.news_sources, name="news_sources"
    # ),  # страница с источниками новостей
    # path(
    #     "news/weather/", views.weather_widget_view, name="weather_widget"
    # ),  # страница с погодой
    # path("news/daily-summary/", views.daily_summary, name="daily-summary"),
]
