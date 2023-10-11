from .models import Post,Like,Comment
from .forms import ProjectForm,CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from users.models import Profile
from .forms import UserCreationForm



@login_required(login_url='login')
def projects(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    projects = Post.objects.filter(owner__username__icontains=search_query)

    # profile = Profile.objects.filter(name__icontains=search_query)

    context = {'projects': projects, 'search_query': search_query}
    return render(request, 'projects/projects.html', context)




@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)




@login_required(login_url='login')
def updateProject(request, pk):

    project = Post.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if request.user == project.owner:
            if form.is_valid():
                form.save()
                return redirect('projects')
        else:
            messages.error(request,"not valid")
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)




@login_required(login_url='login')
def deleteProject(request, pk):
    project = Post.objects.get(id=pk)

    if request.user == project.owner:
        project.delete()
        return redirect('projects')
    else:
        messages.error(request, "not valid")

    context={'object': project}
    return render(request, 'projects/delete_object.html',context)



def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, 'Username OR Password is incorrect')

    return render(request, 'projects/login_register.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account is created')

            login(request, user)
            return redirect('projects')
        else:
            messages.success(
                request, 'an error has occured during registration'
            )

    context = {'page': page, 'form': form}
    return render(request, 'projects/login_register.html', context)

def likeProject(request, pk):
    user = request.user.profile
    post = Post.objects.get(id=pk)
    current_likes = post.like
    liked = Like.objects.filter(user=user, post=post)
    if not liked.exists():
        liked = Like.objects.create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        liked = Like.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
    post.like = current_likes
    post.save()
    return redirect('projects')

def commentProject(request,pk):
    form = CommentForm()

    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)



        comment = form.save(commit=False)
        comment.user = request.user.profile
        comment.post = post
        comment.save()
        return redirect('projects')
    context = {'form': form, 'post': post}
    return render(request, 'projects/comment.html', context)

def ShowComment(request,pk):
    post = Post.objects.get(id=pk)
    print(type(post))

    comments = Comment.objects.filter(post=post)
    context = {'post': post,'comments': comments}
    print(comments)
    return render(request, 'projects/show-comment.html', context)

