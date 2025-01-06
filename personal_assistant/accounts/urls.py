"""Module providing a function printing python version."""
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.messages import success
from django.urls import path
from .views import signupuser, loginuser, logoutuser, ResetPasswordView, CustomPasswordResetConfirmView

app_name = "accounts"

urlpatterns = [
    path("signup/", signupuser, name="signup"),
    path("login/", loginuser, name="login"),
    path("logout/", logoutuser, name="logout"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-password"),
    path("reset-password/done/", PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name="password_reset_done"),
    path("reset-password/confirm/<uidb64>/<token>/",
         CustomPasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path("reset-password/complete/",
         PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name="password_reset_complete"),
    # path('profile/', profile, name='profile'),
]