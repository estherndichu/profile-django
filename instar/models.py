from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = CloudinaryField('profile')
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

     @classmethod
    def search_by_user(cls,search_term):
        instar = cls.objects.filter(user__icontains=search_term)
        return instar   

def create_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

post_save.connect(create_profile, sender = User)

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = CloudinaryField('post')
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    comment = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name} - {self.caption}"

