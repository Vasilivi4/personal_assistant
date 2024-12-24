from django.http import HttpResponse

def index(request):
    return HttpResponse("Добро пожаловать в главный модуль Accounts!")

def login_view(request):
    return HttpResponse("Страница входа")

def signup_view(request):
    return HttpResponse("Страница регистрации")
