from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    contact_no = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile_pics')
    title = models.CharField(max_length=255, blank=True)
    linkedin_url = models.CharField(max_length=100)
    github_url = models.CharField(max_length=50)
    about_me = models.CharField(max_length=500)
    cv = models.FileField(upload_to='cvs/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.username} Profile'
