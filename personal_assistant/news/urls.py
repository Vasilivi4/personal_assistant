from django.urls import path
from personal_assistant.news import views


app_name = "news"

urlpatterns = [
    path("", views.news_list, name="news_list"),
    path("sources/", views.news_sources, name="news_sources"),
]
