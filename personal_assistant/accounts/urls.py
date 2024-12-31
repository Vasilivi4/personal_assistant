"""Module providing a function printing python version."""

from django.urls import path
from accounts.views import signupuser, loginuser, logoutuser

app_name = "accounts"

urlpatterns = [
    path("signup/", signupuser, name="signup"),
    path("login/", loginuser, name="login"),
    path("logout/", logoutuser, name="logout"),
    # path('profile/', profile, name='profile'),
]
