"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("notes/", include("notes.urls")),
    path('', include('news.urls')),
    path('contact/', views.contact_us, name='contact_us'),
    path('terms/', views.terms_and_conditions, name='terms_and_conditions'),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('files/', include('files.urls')),
    path('comments/', include('comments.urls')),
]
