from django.db import models

# Create your models here.
class URL(models.Model):
    original_url=models.URLField(unique=True)
    short_url = models.CharField(max_length=10)