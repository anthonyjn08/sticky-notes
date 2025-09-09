from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating Note objects.

    Fields:
        - title: Charfield, uses nootstrap Text Input for title.
        - content: TextField, uses bootstrap text area for content.
        - priority: IntegerField, uses bootstrp select to swt priority.
    """
    class Meta:
        model = Note
        fields = ["title", "content", "priority"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "priority": forms.Select(attrs={"class": "form-select"}),
        }
