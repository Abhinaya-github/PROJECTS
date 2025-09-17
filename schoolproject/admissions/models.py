from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField( max_length=50)
    fathername=models.CharField( max_length=50)
    classname=models.IntegerField(max_length=15)
    contact=models.CharField(max_length=15)
