from dataclasses import fields
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'author']
    # fields = ['author', 'title', 'text', 'created_date']

admin.site.register(Post, PostAdmin)
