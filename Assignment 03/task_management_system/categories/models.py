from django.db import models
# from task.models import Task
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name