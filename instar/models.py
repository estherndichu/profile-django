from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = CloudinaryField('profile')
    bio = models.CharField(max_length=200, blank=True)
    name =models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def search_by_user(cls,name):
        return cls.objects.filter(user__username__icontains=name).all()

def create_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

post_save.connect(create_profile, sender = User)

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = CloudinaryField('post')
    name = models.CharField(max_length=50, blank=True)
    caption = models.CharField(max_length=100, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.caption}"

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    

class Comment(models.Model):
    comment = models.TextField(max_length=256)
    post =models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(Profile,on_delete= models.CASCADE)

    def __str__(self):
        return self.user.name

class Follow(models.Model):
    follower = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'     