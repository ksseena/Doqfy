from django.db import models

class Snippet(models.Model):
    content = models.TextField()
    secret_key = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
