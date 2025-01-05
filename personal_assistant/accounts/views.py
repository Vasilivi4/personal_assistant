"""Module providing a function printing python version."""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import RegisterForm, LoginForm


def signupuser(request):
    """Function signupuser printing python version."""
    if request.user.is_authenticated:
        return redirect(to='news:index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='news:index')
        else:
            return render(request,'accounts/signup.html', {'form': form})

    return render(request,'accounts/signup.html', context={'form': RegisterForm()})

def loginuser(request):
    """Function loginuser printing python version."""
    if request.user.is_authenticated:
        return redirect(to='news:index')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password did\'t match')
            return redirect(to='accounts:login')

        login(request, user)
        return redirect(to='news:index')

    return render(request, 'accounts/login.html', context={'form': LoginForm()})

@login_required
def logoutuser(request):
    """Function loginuser printing python version."""
    logout(request)
    return redirect(to='news:index')
