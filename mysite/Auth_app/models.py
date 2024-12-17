from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    age=models.IntegerField()
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField()
    