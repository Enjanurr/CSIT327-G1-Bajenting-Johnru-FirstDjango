from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


###


class CustomUser(AbstractUser):
    # Add any additional fields you want for your custom user model

    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        INSTRUCTOR = "INSTRUCTOR", "Instructor"
        ADMIN = "ADMIN", "Administrator"

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT
    )

    course = models.CharField(
        max_length=100, 
        blank=True 
    )
