from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UserFile

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = UploadFileForm()
    return render(request, 'files/upload.html', {'form': form})

def file_list(request):
    category = request.GET.get('category', 'all')
    if category == 'all':
        files = UserFile.objects.all()
    else:
        files = UserFile.objects.filter(category=category)
    return render(request, 'files/file_list.html', {'files': files, 'category': category})
