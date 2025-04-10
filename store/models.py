
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='book_images/', blank=True)

    def __str__(self):
        return self.title
