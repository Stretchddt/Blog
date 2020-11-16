from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Welcome to Blogify!')
    email = models.EmailField(max_length=200, blank=True, default='None')
    country = models.CharField(max_length=100, blank=True, default='None')
    avatar = models.ImageField(default='blogify.jpg', upload_to='profile_photos/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}-{self.middle_name}-{self.last_name}'