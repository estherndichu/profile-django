from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = CloudinaryField('photo')
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    comment = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name} - {self.caption}"