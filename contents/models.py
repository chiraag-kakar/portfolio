from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    contact_no = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    image = models.ImageField(help_text='425x425px recommmended', upload_to='profile_pics')
    title = models.CharField(max_length=100, blank=True)
    linkedin_url = models.CharField(max_length=100)
    github_url = models.CharField(max_length=50)
    about_me = models.CharField(max_length=500)
    cv_link = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # Override the save function in Profile class:
    def save(self, *args, **kwargs):
        # run the parent class' save() function:
        super().save(*args, **kwargs)

        # open the image of the current instance:
        img = Image.open(self.image.path)

        if img.height > 425 or img.width > 425:
            output_size = (425, 425)
            img.thumbnail(output_size)
            img.save(self.image.path)


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
    level = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    achievements = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.level} - {self.school}'


class WorkExperience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    summary = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.position} - {self.company}'


class ProjectCategory(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20, blank=True)
    description = models.TextField()
    date_started = models.CharField(max_length=20, blank=True)
    date_ended = models.CharField(max_length=20, blank=True)
    main_image = models.ImageField(upload_to='project_images', default='')
    repo_link = models.CharField(max_length=50, blank=True)
    demo_link = models.CharField(max_length=50, blank=True)
    document_link = models.CharField(max_length=255, blank=True)
    project_category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title


class ToolsAndTech(models.Model):
    name = models.CharField(max_length=30)
    project = models.ManyToManyField(Project, related_name='toolsandtechs')

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project_images')
    caption = models.CharField(max_length=100, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projectimages')

    def __str__(self):
        return f'{self.project.code} - {self.image.name}'


class Recommendation(models.Model):
    name = models.CharField(max_length=40)
    message = models.CharField(max_length=400)
    image = models.ImageField(upload_to='recommendations', default='recommendations/default')
    summary = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.name} - {self.summary}'


class Certification(models.Model):
    title = models.CharField(max_length=100)
    authority = models.CharField(max_length=30)
    date_issued = models.CharField(max_length=20)
    document_link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Seminar(models.Model):
    title = models.CharField(max_length=100)
    organizer = models.CharField(max_length=30)
    event_date = models.CharField(max_length=20)
    link_proof = models.CharField(max_length=200, blank=True)
    link_icon = models.CharField(max_length=20, blank=True)
    document_link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
