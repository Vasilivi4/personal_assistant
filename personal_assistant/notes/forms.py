from django import forms
from .models import Note


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
