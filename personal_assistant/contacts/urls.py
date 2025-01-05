from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contacts/', views.index, name='contacts'),  # Головна сторінка
    path('contact/create/', views.contact_create, name='contact_create'),
    path('contact/edit/<int:pk>/', views.contact_edit, name='contact_edit'),
    path('contact/delete/<int:pk>/', views.contact_delete, name='contact_delete'),
]