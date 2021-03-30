from django.shortcuts import render,redirect
from .models import Post, Profile
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
from django.http import HttpResponseRedirect

def index(request):
    images = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    params = {
        'images': images,
        'form': form,
        'users': users,

    }
    return render(request, 'instar/index.html', params)
    