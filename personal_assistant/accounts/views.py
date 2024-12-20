from django.http import HttpResponse

def home(request):
    return HttpResponse("Добро пожаловать на главную страницу!")
