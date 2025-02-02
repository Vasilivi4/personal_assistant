"""URLs for the portfolio app."""

from django.urls import path
from portfolio.views import portfolio

app_name = "portfolio"

urlpatterns = [
    path("", portfolio, name="portfolio"),
]
