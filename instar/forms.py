from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'caption')


class UserForm(forms.ModelForm):
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control mb-3","placeholder":"First Name"}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control mb-3","placeholder":"Last Name"}))
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control mb-3","placeholder":"Username"}))
    email = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control mb-3","placeholder":"Email"}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"class":"form-control mb-3","placeholder":"Password"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password",)

    


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("photo",)
