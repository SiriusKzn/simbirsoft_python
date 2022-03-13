from .models import Notes
from django.forms import ModelForm, TextInput, DateTimeField, IntegerField


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title']
        widgets = {
            "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Текст заметки'
        }),
       }