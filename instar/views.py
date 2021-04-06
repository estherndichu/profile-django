from django.shortcuts import render,redirect
from .models import Post, Profile, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm, ProfileForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def index(request):
    current_user = request.user.profile
    posts = Post.objects.all()[::-1]
    comments = Comment.objects.all()
    users = User.objects.exclude(id=request.user.id)

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)

            post.profile = current_user

            post.save()
            post_form = PostForm()
            return HttpResponseRedirect(reverse("index"))

    else:
        post_form = PostForm()

    return render(request, "instar/index.html", context={"posts":posts,"current_user":current_user,"post_form":post_form,"comments":comments})

def post(request, id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post__id=id)
    current_user = request.user
    current_profile = Profile.objects.get(post=id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = current_user
            comment.post = post
            comment.save()
            comment_form = CommentForm()
            return redirect("post", post.id)

    else:
        comment_form = CommentForm()

    return render(request, "instar/post.html", context={"post":post,"current_user":current_user,"current_profile":current_profile,"comment_form":comment_form,"comments":comments,}) 

def like(request, id):
    post = Post.objects.get(id = id)
    post.likes +=1
    post.save()
    return HttpResponseRedirect(reverse("index"))  
    
@login_required()
def profile(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=user)
    posts = Post.objects.filter(profile__id=id)[::-1]
    return render(request, "instar/profile.html",{"user":user, "profile":profile, "posts":posts})

def search(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get('search_user')
        results = Profile.search_by_user(name)
        message = f"{name}"

        return render(request,'instar/search.html',{"results":results,"message":message})

    else: 
        message = f"You haven't searched yet"
        return render (request,'instar/search.html',{"message":message})

def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponseRedirect(reverse("user_login"))

        else:
            return HttpResponseRedirect(reverse("user_login"))
    else:
        return render(request, "registration/login.html", context={})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user_login"))

def follow(request, to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=user_profile3)
        follow_s.save()
        return redirect('profile', user_profile3.user.username)

def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile2 = Profile.objects.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=user_profile2)
        unfollow_d.delete()
        return redirect('profile', user_profile2.user.username)        