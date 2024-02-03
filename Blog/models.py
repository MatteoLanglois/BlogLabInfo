from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
import django.utils.timezone
import datetime

from django.db.models import SET_NULL


class Theme(models.Model):
    theme_name = models.CharField(max_length=100)
    theme_icon = models.CharField(max_length=100)

    def __str__(self):
        return self.theme_name

    def print_icon(self):
        return f"<i class='theme-icon {self.theme_icon}'></i>"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400, null=True, blank=True)
    date = models.DateField(default=django.utils.timezone.now)
    content = RichTextField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    theme = models.ForeignKey('Theme', on_delete=SET_NULL, null=True, blank=True
                              , related_name='Blogs')
    visible = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_content(self):
        return self.content.order_by('position').all()


class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE,
                             related_name='comments', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='replies', null=True, blank=True)
    name = models.CharField(max_length=200)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment
