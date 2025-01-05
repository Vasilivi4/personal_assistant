# files/views.py
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile

# Уявлення для завантаження файлів
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)  # Обробка POST-запиту
        if form.is_valid():  # Перевірка валідності форми
            form.save()  # Збереження файлу в базі даних
            return redirect('file_list')  # Перенаправлення на список файлів
    else:
        form = UploadFileForm()  # Порожня форма для GET-запиту
    return render(request, 'files/upload.html', {'form': form})  # Рендер сторінки

# Уявлення для списку файлів
def file_list(request, category=None):
    if category == 'all':  # Якщо категорія "всі", відобразити всі файли
        files = UploadedFile.objects.all()
    else:  # Інакше - фільтрувати за категорією
        files = UploadedFile.objects.filter(category=category)
    return render(request, 'files/file_list.html', {'files': files, 'category': category})
