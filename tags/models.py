from django.db import models
from posts.models import Post
from django.shortcuts import reverse


class Tag(models.Model):
    title = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, related_name='tags')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'id': self.id})