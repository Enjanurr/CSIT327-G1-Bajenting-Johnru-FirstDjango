from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        INSTRUCTOR = 'INSTRUCTOR', 'Instructor'
        ADMIN = 'ADMIN', 'Administrator'
    email = models.EmailField('email address', unique=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.STUDENT) 
    course = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} by {self.user.username}"