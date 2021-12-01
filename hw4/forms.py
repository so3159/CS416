from .models import Todo
from django import forms


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Add tasks"
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': "switch"
            })
        }
