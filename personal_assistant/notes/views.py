from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note, Tag
from django import forms


# Form for Notes
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "tags"]
        widgets = {"tags": forms.CheckboxSelectMultiple()}


# List all notes
@login_required
def note_list(request):
    notes = Note.objects.filter(user_id=request.user.id)
    return render(
        request,
        "notes/note_list.html",
        {
            "notes": notes,
        },
    )


# Create new note
@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user_id = request.user.id
            note.save()
            form.save_m2m()  # Save tags
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form, "action": "Create"})


# Edit existing note
@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user_id=request.user.id)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)

    return render(
        request, "notes/note_form.html", {"form": form, "note": note, "action": "Edit"}
    )


# Delete note
@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user_id=request.user.id)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")

    return render(request, "notes/note_confirm_delete.html", {"note": note})


# Toggle note done status
@login_required
def note_toggle_done(request, pk):
    note = get_object_or_404(Note, pk=pk, user_id=request.user.id)
    note.done = not note.done
    note.save()
    return redirect("note_list")


# Tag management
@login_required
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "notes/tag_list.html", {"tags": tags})
