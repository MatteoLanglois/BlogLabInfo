from django.contrib import admin
from .models import Comment, Blog, Theme
from .forms import BlogForm


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'author', 'theme')
    form = BlogForm


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'date')


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('theme_name', )


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Theme, ThemeAdmin)
