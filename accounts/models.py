from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        INSTRUCTOR = 'INSTRUCTOR', 'Instructor'
        ADMIN = 'ADMIN', 'Administrator'
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.STUDENT) 
    course = models.CharField(max_length=100, blank=True)
    