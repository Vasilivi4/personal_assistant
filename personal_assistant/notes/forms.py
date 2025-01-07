from django import forms
from .models import Note, Tag


class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['tags'].queryset = Tag.objects.filter(user=self.user)

    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']
