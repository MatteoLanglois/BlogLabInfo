from django import forms
from .models import Blog, Comment
import datetime


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'author', 'theme', 'content']
        exclude = ['date']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        date = datetime.date.today()
        if not title and not description and not date:
            raise forms.ValidationError('You have to write something!')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
        labels = {
            'name': '',
            'comment': ''
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3,
                                             'placeholder': 'Votre commentaire'}),
            'name': forms.TextInput(attrs={'placeholder': 'Votre pseudonyme'})
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        comment = cleaned_data.get('comment')
        if not name and not comment:
            raise forms.ValidationError('You have to write something!')
