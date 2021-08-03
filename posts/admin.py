from django.contrib import admin
from blog.posts.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'body', ]

admin.site.register(Post, PostAdmin)
