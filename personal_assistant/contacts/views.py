from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm, ContactSearchForm
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    form = ContactSearchForm(request.GET)
    contacts = Contact.objects.filter(user=request.user).all() if request.user.is_authenticated else []

    # Фільтрація контактів за запитом
    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            contacts = contacts.filter(
                name__icontains=query  # Пошук за ім'ям
            ) | contacts.filter(
                phone__icontains=query  # Пошук за номером телефону
            ) | contacts.filter(
                email__icontains=query  # Пошук за email
            )

    # Логіка для нагадування про дні народження
    today = timezone.now().date()
    reminder_date = today + timedelta(days=7)
    birthday_contacts = Contact.objects.filter(
        birthday__range=(today, reminder_date)  # Контакти з днями народження протягом наступних 7 днів
    )

    return render(request, 'contacts/hom_contact.html', {
        'contacts': contacts,
        'form': form,
        'birthday_contacts': birthday_contacts
    })

@login_required
def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts:contacts")
    else:
        form = ContactForm()
    return render(request, "contacts/contact_form.html", {"form": form})

@login_required
def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contacts:contacts")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/contact_form.html", {"form": form})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contacts:contacts")  # Після видалення перенаправляємо на головну сторінку
    return render(request, "contacts/contact_confirm_delete.html", {"contact": contact})