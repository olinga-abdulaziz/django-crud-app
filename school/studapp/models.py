from django.db import models

# Create your models here.

class Student(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    form=models.CharField(max_length=10)
    dorm=models.CharField(max_length=100)
    parent_name=models.CharField(max_length=100)

    def __str__(self):
        return self.fname +' '+ self.lname

class Parent(models.Model):
    parent_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    home=models.CharField(max_length=100)

    def __str__(self):
        return self.parent_name
