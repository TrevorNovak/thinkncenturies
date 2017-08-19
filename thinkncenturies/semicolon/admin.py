from django.contrib import admin
from semicolon.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'genre',
        'body',
    ]

admin.site.register(Post, PostAdmin)
