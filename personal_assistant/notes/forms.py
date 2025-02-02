"""Module for forms in the notes app"""

from django import forms
from notes.models import Note, Tag


class NoteForm(forms.ModelForm):
    """Class NoteForm representing a person"""

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields["tags"].queryset = Tag.objects.filter(user=self.user)

    class Meta:
        """Class Meta representing a person"""

        model = Note
        fields = ["title", "content", "tags"]
