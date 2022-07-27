from enum import unique
from django.db import models
from django.forms import CharField

# Create your models here.
class Component(models.Model):
    name=models.CharField(max_length=15)
    status=models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.name

