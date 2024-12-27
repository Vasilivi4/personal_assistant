from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm


# Create your views here.
def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='index')
        else:
            return render(request,'accounts/signup.html', {'form': form})

    return render(request,'accounts/signup.html', context={'form': RegisterForm()})

def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='index')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password did\'t match')
            return redirect(to='accounts:login')

        login(request, user)
        return redirect(to='index')

    return render(request, 'accounts/login.html', context={'form': LoginForm()})

@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='index')
