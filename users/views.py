from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from users.models import Profile, Follow
from instaprojects.models import Post

from django.contrib.auth.models import User
from .forms import ProfileForm



def userProfile(request):

    profiles = request.user.profile

    context = {'profiles': profiles}
    return render(request, 'users/user-profile.html', context)

def editAccount(request):
    profiles = request.user.profile
    form = ProfileForm(instance=profiles)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profiles)
        if form.is_valid():
            form.save()
            return redirect('user-profile')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

def singleProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    user= request.user
    context = {'profile': profile, 'user':user}

    return render(request, 'users/single-profile.html', context)

def follow(request, pk):
    user = Profile.objects.get(id=pk)
    Follow.objects.get_or_create(follower=request.user.profile, followed=user)
    return redirect('single-profile', pk=pk)

def unfollow(request, pk):
    user = Profile.objects.get(id=pk)
    follow = Follow.objects.filter( follower=request.user.profile, followed=user)
    if follow.exists():
        follow.delete()
    return redirect('single-profile', pk=pk)

def followers(request,pk):

     user = Profile.objects.get(id=pk)
     follow = Follow.objects.filter(follower=user)
     context = {'follow': follow}
     return render(request, 'users/followers.html', context)


def following(request, pk):
    user = Profile.objects.get(id=pk)
    follow = Follow.objects.filter(followed=user)
    context = {'follow': follow}
    return render(request, 'users/following.html', context)



