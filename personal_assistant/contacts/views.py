"""This module contains views for the contacts app."""

from datetime import timedelta, date
from contacts.models import Contact
from contacts.forms import ContactForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def contacts_list(request):
    """Function contacts_list printing python version."""
    today = date.today()

    default_days = 7
    end_date = today + timedelta(days=default_days)

    query = request.GET.get("query", "")
    month_number = request.GET.get("number", "")
    days_left = request.GET.get("days", "")

    try:
        days_left = int(days_left) if days_left else default_days
    except ValueError:
        days_left = default_days

    try:
        month_number = int(month_number) if month_number else None
    except ValueError:
        month_number = None

    contacts = Contact.objects.all()

    if query:
        contacts = contacts.filter(name__icontains=query)

    if month_number is not None:
        contacts = contacts.filter(birthday__month=month_number)

    start_date = today
    end_date = today + timedelta(days=days_left)
    birthday_contacts = Contact.objects.filter(
        birthday__month__gte=start_date.month,
        birthday__day__gte=start_date.day,
        birthday__month__lte=end_date.month,
        birthday__day__lte=end_date.day,
    )

    return render(
        request,
        "contacts/contacts_list.html",
        {
            "contacts": contacts,
            "birthday_contacts": birthday_contacts,
            "days_left": days_left,
        },
    )


@login_required
def contact_create(request):
    """Function contact_create printing python version."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect("contacts:contacts_list")
    else:
        form = ContactForm()
    return render(request, "contacts/contact_form.html", {"form": form})


@login_required
def contact_edit(request, pk):
    """Function contact_edit printing python version."""
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contacts:contacts_list")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/contact_form.html", {"form": form})


@login_required
def contact_delete(request, pk):
    """Function contact_delete printing python version."""
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contacts:contacts_list")
    return render(request, "contacts/contact_confirm_delete.html", {"contact": contact})
