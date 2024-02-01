from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
import datetime


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400, null=True, blank=True)
    date = models.DateField(default=datetime.date.today())
    content = RichTextField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)

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
