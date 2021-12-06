from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group



class CustomGroup(Group):
    # groupname = models.CharField(max_length=120)

    def __str__(self):
        # return self.groupname
        return self.name


class CustomUser(AbstractUser):
    # group = models.ManyToManyField(CustomGroup, blank=True, related_name="user_group")
    
    def __str__(self):
        return self.username


class Task(models.Model):
    taskname = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline_at = models.DateTimeField(blank=True, null=True)
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_task")
    group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.taskname

