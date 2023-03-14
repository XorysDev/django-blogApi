from django.db import models
from category.models import Category


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField(blank=True)

    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')

    preview = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner} --> {self.title[:50]}'

    class Meta:
        ordering = ('created_at',)