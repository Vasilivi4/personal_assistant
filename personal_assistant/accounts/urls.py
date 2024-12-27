from django.urls import path
from .views import signupuser, loginuser, logoutuser

app_name = 'accounts'

urlpatterns = [
    path('signup/', signupuser, name='signup'),
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
    # path('profile/', profile, name='profile'),
    ]
