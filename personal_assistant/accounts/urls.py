from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница для accounts http://127.0.0.1:8000/accounts/
    path('login/', views.login_view, name='login'),#http://127.0.0.1:8000/accounts/login/
    path('signup/', views.signup_view, name='signup'),#http://127.0.0.1:8000/accounts/signup/
]
