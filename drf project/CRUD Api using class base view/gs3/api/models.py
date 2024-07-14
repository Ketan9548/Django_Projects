from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100,default="")
    roll = models.IntegerField()
    city = models.CharField(max_length=200,default="")