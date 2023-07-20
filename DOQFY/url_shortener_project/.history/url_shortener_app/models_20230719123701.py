from django.db import models

# Create your models here.
class URL(models.Model):
    original_url=models.URLField(unique=True)
    short_url = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.short_url