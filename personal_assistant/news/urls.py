"""Module providing a function printing python version."""

from django.urls import path
from news import views


app_name = "news"

urlpatterns = [
    path('', views.index, name='index'),
    path('news/list/', views.news_list, name='news_list'),
    path('news/sources/', views.news_sources, name='news_sources'),
]
