from django.shortcuts import render,redirect
from .models import Post, Profile
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
from django.http import HttpResponseRedirect

def index(request):
    posts = Post.objects.all()[::-1]

    return render(request, "instar/index.html", {"posts":posts})