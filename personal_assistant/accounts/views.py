"""Module providing a function printing python version."""
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm


def signupuser(request):
    """Function signupuser with username existence check."""
    if request.user.is_authenticated:
        return redirect(to='news:index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Користувач із такою електронною поштою вже існує.')
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Користувач із таким іменем уже існує.')
            else:
                form.save()
                return redirect(to='news:index')
        return render(request, 'accounts/signup.html', {'form': form})

    return render(request, 'accounts/signup.html', context={'form': RegisterForm()})


def loginuser(request):
    """Function loginuser printing python version."""
    if request.user.is_authenticated:
        return redirect(to='news:index')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='accounts:login')

        login(request, user)
        return redirect(to='news:index')

    return render(request, 'accounts/login.html', context={'form': LoginForm()})


@login_required
def logoutuser(request):
    """Function loginuser printing python version."""
    logout(request)
    return redirect(to='news:index')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    """Class ResetPasswordView printing python version."""
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