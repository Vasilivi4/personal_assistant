from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('notes/', include('notes.urls')),
    path('files/', include('files.urls')),
    path('news/', include('news.urls')),
]
