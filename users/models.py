from django.db import models
from django.contrib.auth.models import AbstractUser

#Custom User model extending Django's AbstractUse
class User(AbstractUser):
    #User's full name
    name = models.CharField(max_length=100)
    #User's gender
    gender = models.CharField(max_length=10)
    
    #Available user roles
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
    )
    #User role (defaults to student)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    #Required fields when creating a superuser
    REQUIRED_FIELDS=['name','gender']
    #String representation of the user
    def __str__(self):
        return self.username


