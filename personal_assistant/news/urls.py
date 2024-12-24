from django.urls import path
from news import views


app_name = "news"

urlpatterns = [
    path("", views.news_list, name="news_list"),
    path("sources/", views.news_sources, name="news_sources"),
    path('weather/', views.weather_widget_view, name='weather_widget'),
]
