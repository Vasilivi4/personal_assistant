from django.urls import path
from comments import views

app_name = 'comments'

urlpatterns = [
    path('post/<int:post_id>/', views.comment_list, name='comment_list'),
]