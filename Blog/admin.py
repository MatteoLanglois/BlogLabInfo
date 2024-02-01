from django.contrib import admin
from .models import Comment, Blog
from .forms import BlogForm


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'author')
    form = BlogForm


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'date')


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
