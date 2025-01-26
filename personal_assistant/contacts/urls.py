"""Module providing a function printing python version."""

from django.urls import path
from contacts import views

app_name = 'contacts'

urlpatterns = [
    path('', views.contacts_list, name='contacts_list'),
    path('create/', views.contact_create, name='contact_create'),
    path('<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('<int:pk>/delete/', views.contact_delete, name='contact_delete'),
]