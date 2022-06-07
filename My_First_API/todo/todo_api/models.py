from turtle import update
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class ToDo(models.Model):
    task = models.CharField(max_length=180)
    timestamp = models.DateField(auto_now_add=True,auto_now=False,blank=True)
    completed = models.BooleanField(default=False, blank=True)
    update = models.DateField(auto_now=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.task