from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    published_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    cover = CloudinaryField('image', blank=True, null=True)  # Cloudinary path folder

    def __str__(self):
        return f"{self.title} by {self.author}"

    @property
    def cloud_cover(self):
        if self.cover:
            return self.cover.url   # ✔ correct Cloudinary URL
        return None

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
