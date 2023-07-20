from django.db import models

# Create your models here.
from django.db import models

class Nifty50Data(models.Model):
    company = models.CharField(max_length=200)
    last_price = models.DecimalField(max_digits=10, decimal_places=2)
    change = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.company
