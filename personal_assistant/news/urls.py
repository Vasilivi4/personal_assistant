"""Module providing a function printing python version."""

from django.urls import path
from news import views


app_name = "news"

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.news_list, name='news_list'),
    path('news/sources/', views.news_sources, name='news_sources'),
    path('news/weather/', views.weather_widget_view, name='weather_widget'),
    path('news/daily-summary/', views.daily_summary, name='daily-summary'),
]
