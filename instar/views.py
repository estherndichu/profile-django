from django.shortcuts import render,redirect
from .models import Post, Profile
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.all()[::-1]

    return render(request, "instar/index.html", {"posts":posts})

def post(request,id):
    post = Post.objects.get(id=id)

    return render(request,'instar/post.html', {'post':post})   

def like(request, id):
    post = Post.objects.get(id = id)
    post.likes +=1
    post.save()
    return HttpResponseRedirect(reverse("index"))  
    

def profile(request, id):
    profile = Profile.objects.get(id=id)
    posts = Post.objects.filter(profile__id=id)[::-1]
    return render(request, "instar/profile.html",{"profile":profile,"posts":posts})

def search(request):
    if 'profile' in request.GET and request.GET['profile']:
        search_term = request.GET.get('profile')
        searched_user = Profile.search_by_user(search_term)
        user = User.objects.all()
        return render(request,'instar/search.html',{"user":user,"profile":searched_user})

    else:
        user = User.objects.all()
        return render (request,'instar/search.html',{"user":user})   