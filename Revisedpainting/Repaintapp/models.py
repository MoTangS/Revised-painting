from django.db import models

# Create your models here.



class repaintUser(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now = True)
    isdelete = models.BooleanField(default=False)