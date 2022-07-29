from enum import unique
from multiprocessing.sharedctypes import Value
from django.db import models
from django.forms import CharField

# Create your models here.
class Component(models.Model):
    name=models.CharField(max_length=15)
    status=models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    name= models.CharField(max_length=15)
    value=models.FloatField(blank=True,default=0)
    unit=models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return self.name
