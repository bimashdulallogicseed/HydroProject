
from django.db import models

# Create your models here.
class hydrosheet(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.FloatField()
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name