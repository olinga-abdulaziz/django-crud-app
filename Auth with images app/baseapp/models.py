from django.db import models
from django.urls import reverse
# Create your models here.
class Records(models.Model):
    caption=models.CharField(max_length=100)
    desc=models.CharField(max_length=200)
    image=models.ImageField(null=True,blank=True, upload_to='images/')


    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('home')