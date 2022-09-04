from django.db import models
from django.contrib.auth.admin import User

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="pictures/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ProfilePicture')

    def __str__(self):
        return f'{self.user.username} Profile'


class Quiz(models.Model):
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    points = models.FloatField()
    done = models.BooleanField()