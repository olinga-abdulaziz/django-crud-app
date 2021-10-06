from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.CharField(max_length=4)
    sname=models.CharField(max_length=255)
    scontact=models.CharField(max_length=255)
    
    def __str__(self):
        return self.sname
