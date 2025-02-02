"""Module notes views."""

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from notes.models import Note, Tag
from notes.forms import NoteForm


def note_list(request):
    """Function note_list printing python version."""
    notes = (
        Note.objects.filter(user=request.user).all()
        if request.user.is_authenticated
        else []
    )
    tags = (
        Tag.objects.filter(user=request.user).all()
        if request.user.is_authenticated
        else []
    )
    query = request.GET.get("q")
    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))
    tag_id = request.GET.get("tag")
    if tag_id:
        notes = notes.filter(tags__id=tag_id)
    return render(
        request,
        "notes/note_list.html",
        {"notes": notes, "tags": tags, "selected_tag": tag_id, "query": query},
    )


@login_required
def note_create(request):
    """Function note_create printing python version."""
    if request.method == "POST":
        form = NoteForm(request.POST, user=request.user)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            form.save_m2m()  # Save tags
            return redirect("notes:note_list")
    else:
        form = NoteForm(user=request.user)
    return render(request, "notes/note_form.html", {"form": form, "action": "Create"})


@login_required
def note_edit(request, pk):
    """Function note_edit printing python version."""
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("notes:note_list")
    else:
        form = NoteForm(instance=note, user=request.user)
    return render(
        request, "notes/note_form.html", {"form": form, "note": note, "action": "Edit"}
    )


@login_required
def note_delete(request, pk):
    """Function note_delete printing python version."""
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("notes:note_list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})


@login_required
def note_toggle_done(request, pk):
    """Function note_toggle_done printing python version."""
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.done = not note.done
    note.save()
    return redirect("notes:note_list")


def tag_list(request):
    """Function tag_list printing python version."""
    tags = (
        Tag.objects.filter(user=request.user).all()
        if request.user.is_authenticated
        else []
    )
    return render(request, "notes/tag_list.html", {"tags": tags})


@login_required
def tag_create(request):
    """Function tag_create printing python version."""
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            if Tag.objects.filter(name__iexact=name, user=request.user).exists():
                return JsonResponse({"success": False, "error": "Tag already exists"})
            tag = Tag.objects.create(name=name, user=request.user)
            return JsonResponse(
                {"success": True, "tag": {"id": tag.id, "name": tag.name}}
            )
    return JsonResponse({"success": False, "error": "Invalid request"})
