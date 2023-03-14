from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='children', blank=True, null=True)

    def __str__(self):
        return f'{self.name} --> {self.parent}' if self.parent else f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

