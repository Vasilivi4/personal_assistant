from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Note, Tag
from django import forms


class NoteForm(forms.ModelForm):
    new_tag = forms.CharField(
        required=False,
        label="Add New Tag",
        widget=forms.TextInput(attrs={"placeholder": "Enter new tag name"}),
    )

    class Meta:
        model = Note
        fields = ["title", "content", "tags"]
        widgets = {"tags": forms.CheckboxSelectMultiple()}


def note_list(request):
    notes = Note.objects.all()
    tags = Tag.objects.all()
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


def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            # Handle new tag creation
            new_tag_name = form.cleaned_data.get("new_tag")
            if new_tag_name:
                tag, created = Tag.objects.get_or_create(name=new_tag_name)
                if created:
                    form.data = form.data.copy()
                    form.data.setlist("tags", list(form.data.getlist("tags")) + [str(tag.id)])
            
            note = form.save(commit=False)
            note.user_id = 1
            note.save()
            form.save_m2m()
            return redirect("notes:note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form, "action": "Create"})


def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes:note_list")
    else:
        form = NoteForm(instance=note)
    return render(
        request, "notes/note_form.html", {"form": form, "note": note, "action": "Edit"}
    )


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("notes:note_list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})


def note_toggle_done(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.done = not note.done
    note.save()
    return redirect("notes:note_list")


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "notes/tag_list.html", {"tags": tags})


def tag_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Tag.objects.create(name=name)
    return redirect("notes:note_list")
