from django.db import models
from django.urls import reverse  
from django.contrib.auth.models import User 

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 150)
    author = models.CharField(max_length= 150)
    issn = models.IntegerField()
    vol = models.IntegerField()
    coverImage = models.CharField(max_length=1500 )
    status = models.BooleanField(default= False)
    
    def __str__(self):
        
        return self.title