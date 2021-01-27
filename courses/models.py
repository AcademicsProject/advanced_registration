from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    id = models.CharField(max_length=5 , primary_key=True)
    name = models.CharField(max_length=100)
    stream = models.CharField(max_length=32)
    strength = models.IntegerField()
    description = models.CharField(max_length=255)
    teacher = models.CharField(max_length=100)
    enrollee = models.ManyToManyField(User, related_name="student", blank=True) 

    def __str__(self):
        return self.name

