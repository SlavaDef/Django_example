from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


# клас для роботи з юзером, ніби приймання данних у бд з форми введення юзера
class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'content', 'date'] # всі поля з бд

        # опис інпутів
        widgets = {
             'title': TextInput(attrs={'class':'form-control', 'placeholder':'Назва статті'}),
             'anons': TextInput(attrs={'class': 'form-control', 'placeholder': 'Анонс'}),
             'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'текст статті'}),
             'date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),

        }