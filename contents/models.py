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


class Focus(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=20)
    color = models.CharField(max_length=20, default='white')
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - Active: {self.is_active}'


class TechnicalSkill(models.Model):
    name = models.CharField(max_length=20)
    is_top_skill = models.BooleanField(default=True)
    percentage = models.IntegerField()

    def __str__(self):
        return f'{self.name} - Top Skill: {self.is_top_skill}'


class ProfessionalSkill(models.Model):
    name = models.CharField(max_length=20)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name


class Education(models.Model):
    school = models.CharField(max_length=100)
    duration = models.CharField(max_length=15)
    level = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    achievements = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.level} - {self.school}'


class WorkExperience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.position} - {self.company}'

