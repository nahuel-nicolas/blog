from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)
    slug = models.SlugField(unique=True, blank=True, default='autogenerated-slug')
    # ['author', 'title', 'text', 'created_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == 'autogenerated-slug':
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Comment(models.Model):
    # post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    
