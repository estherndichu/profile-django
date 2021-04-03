from django.shortcuts import render,redirect
from .models import Post, Profile
from django.contrib.auth.decorators import login_required
from .forms import PostForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

# @login_required(login_url='/accounts/login/')
def index(request):
    # current_user = request.user
    # print(current_user)
    # current_profile = Profile.objects.get(user_id=current_user)
    # posts = Post.objects.all()[::-1]

    # if request.method == "POST":
    #     post_form = PostForm(request.POST, request.FILES)

    #     if post_form.is_valid():
    #         post = post_form.save(commit=False)

    #         post.profile = current_user
    #         post.user_profile = current_profile

    #         post.save()
    #         post_form = PostForm()
    #         return HttpResponseRedirect(reverse("index"))

    # else:
    #     post_form = PostForm()

    

    # return render(request, "instar/index.html",{"posts":posts,"current_user":current_user,"current_profile":current_profile,"post_form":post_form})
    return render(request,'instar/index.html')


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


def register(request):
    registered = False
    

    if request.method == "POST":
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = Profile()
            user_profile.user = user
            user_profile.save()
            registered = True
            
            return HttpResponseRedirect(reverse("user_login"))

        else:
            pass

    else:
        user_form = UserForm()
        

    return render(request, "registration/register.html",{"user_form":user_form,"registered":registered})