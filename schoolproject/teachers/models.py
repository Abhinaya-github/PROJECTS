from django.db import models

# Create your models here.
class Teacher(models.Model):
    name=models.CharField( max_length=50)
    subject=models.CharField( max_length=50)
    experience=models.IntegerField(max_length=15)
    contact=models.CharField(max_length=15)