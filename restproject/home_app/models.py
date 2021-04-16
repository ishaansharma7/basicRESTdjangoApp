from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    mother_tongue = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Task(models.Model):
    task = models.CharField(max_length=250, null=True, blank=True)
    completed = models.BooleanField(default=False,null=True, blank=True)
    
    def __str__(self):
        return self.task
    