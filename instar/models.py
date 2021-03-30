from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = CloudinaryField('photo')
    bio = models.CharField(max_length=500)

    def __str__(self):
        return self.bio

class Comments(models.Model):
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.comment

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=100)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.ManyToManyField(Comments)

    def __str__(self):
        return f"{self.name} - {self.caption}"