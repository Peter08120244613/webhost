from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    reg=models.TextField()
    email=models.EmailField()
    gen=models.CharField(max_length=50)
    stuClass=models.TextField()
    