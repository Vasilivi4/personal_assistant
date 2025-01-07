from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import File
from .forms import FileUploadForm
import logging

logger = logging.getLogger(__name__)


def file_list(request):
    category = request.GET.get('category', None)
    if category:
        files = File.objects.filter(user=request.user, category=category).all() if request.user.is_authenticated else []
    else:
        files = File.objects.filter(user=request.user).all() if request.user.is_authenticated else []
    return render(request, 'files/file_list.html', {'files': files})

@login_required
def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                file = form.save(commit=False)
                file.user = request.user
                logger.info("Attempting to save file to Cloudinary")
                file.save()
            except Exception as e:
                logger.error(f"Error while uploading file: {str(e)}")
                return render(request, 'files/upload.html', {'form': form, 'error': str(e)})
            return redirect('files:file_list')
        else:
            logger.error(f"Form errors: {form.errors}")
    else:
        form = FileUploadForm()
    return render(request, 'files/upload.html', {'form': form})

