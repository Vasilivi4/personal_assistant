from django.shortcuts import render, redirect, get_object_or_404
from contacts.models import Contact
from contacts.forms import ContactForm, ContactSearchForm
from datetime import timedelta
from django.utils import timezone

def get_index(request):
    form = ContactSearchForm(request.GET)
    contacts = Contact.objects.all()

    # Фільтрація контактів за запитом
    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            contacts = contacts.filter(name__icontains=query)

    # Додатково можна додати логіку для нагадування про день народження
    today = timezone.now().date()
    reminder_date = today + timedelta(days=7)
    birthday_contacts = Contact.objects.filter(birthday=reminder_date)

    return render(request, 'contacts/hom_contact.html', {
        'contacts': contacts,
        'form': form,
        'birthday_contacts': birthday_contacts
    })

def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ContactForm()
    return render(request, "contacts/contact_form.html", {"form": form})

def contact_edit(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/contact_form.html", {"form": form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("index")  # Після видалення перенаправляємо на головну сторінку
    return render(request, "contacts/contact_confirm_delete.html", {"contact": contact})
