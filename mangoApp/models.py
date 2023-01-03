from datetime import timezone
from django.db import models
from datetime import datetime

# Create your models here.
class PostUser(models.Model):
    adminId = models.IntegerField(primary_key=True)
    adminPass = models.CharField(max_length=20)
    upload_date = models.DateTimeField(
            default=timezone)
    img = models.ImageField(upload_to="img/",null=True , blank=True)
    def __str__(self):
        return self.adminId 
    
    
class user(models.Model):
    userId = models.CharField(max_length=20 , primary_key=True)
    userPass = models.CharField(max_length=20)
    def __str__(self):
        return self.userId
    
