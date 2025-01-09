"""Module providing a function printing python version."""

from django.shortcuts import render, redirect, get_object_or_404
from contacts.models import Contact
from contacts.forms import ContactForm, ContactSearchForm
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def index(request):
    """Function index printing python version."""
    form = ContactSearchForm(request.GET)
    contacts = Contact.objects.filter(user=request.user).all() if request.user.is_authenticated else []

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            contacts = contacts.filter(
                name__icontains=query
            ) | contacts.filter(
                phone__icontains=query
            ) | contacts.filter(
                email__icontains=query
            )

    today = timezone.now().date()
    reminder_date = today + timedelta(days=7)
    birthday_contacts = Contact.objects.filter(
        birthday__range=(today, reminder_date)
    )

    return render(request, 'contacts/hom_contact.html', {
        'contacts': contacts,
        'form': form,
        'birthday_contacts': birthday_contacts
    })

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('contacts:contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})


@login_required
def contact_edit(request, pk):
    """Function contact_edit printing python version."""
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
    """Function contact_delete printing python version."""
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contacts:contacts")
    return render(request, "contacts/contact_confirm_delete.html", {"contact": contact})