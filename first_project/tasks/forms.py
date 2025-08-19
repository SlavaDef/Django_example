from .models import Task
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput


# клас для роботи з юзером, ніби приймання данних у бд з форми введення юзера
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']  # всі поля з бд

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Task_name'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Task_description'}),
            'completed': CheckboxInput(attrs={'class': 'form-check-input', 'style': 'width: 20px; height: 20px;' })

        }