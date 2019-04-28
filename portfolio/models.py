from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(blank=True,max_length=225)
    age=models.IntegerField(blank=True)
    major=models.CharField(blank=True,max_length=200)
    grade=models.IntegerField(blank=True)
    hometown=models.CharField(blank=True,max_length=200)
    
    