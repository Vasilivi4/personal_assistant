from django.http import HttpResponse

def index(request):
    return HttpResponse("Добро пожаловать в главный модуль Accounts!http://127.0.0.1:8000/contacts/")

def login_view(request):
    return HttpResponse("Страница входа")

def signup_view(request):
    return HttpResponse("Страница регистрации")
