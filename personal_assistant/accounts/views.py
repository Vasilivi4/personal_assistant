"""Module providing a function for user registration and login."""

from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from accounts.forms import RegisterForm, LoginForm


def signupuser(request):
    """Function signupuser with username existence check."""
    if request.user.is_authenticated:
        return redirect(to='news:index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')

            if User.objects.filter(email=email).exists():
                form.add_error('email', 'A user with this email already exists.')
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'A user with this username already exists.')

            if form.errors:
                return render(request, 'accounts/signup.html', {'form': form})

            user = form.save()
            login(request, user)

            messages.success(request, 'You have successfully registered and logged in.')

            return redirect(to='news:index')
        else:
            return render(request, 'accounts/signup.html', {'form': form})

    return render(request, 'accounts/signup.html', context={'form': RegisterForm()})


def loginuser(request):
    """Function loginuser with authentication and error handling."""
    if request.user.is_authenticated:
        return redirect(to='news:index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect(to='accounts:login')

        login(request, user)
        messages.success(request, 'Welcome, you have successfully logged in.')
        return redirect(to='news:index')

    return render(request, 'accounts/login.html', context={'form': LoginForm()})


@login_required
def logoutuser(request):
    """Function logoutuser with user logout handling."""
    logout(request)
    return redirect(to='news:index')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    """Class ResetPasswordView for handling password reset."""
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    html_email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    success_message = 'Password reset link has been sent to your email address. %(email)s'
    subject_template_name = 'accounts/password_reset_subject.txt'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
