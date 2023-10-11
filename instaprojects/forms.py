from django.forms import ModelForm
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectForm(ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'image', 'video']
        exclude = ['owner']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comments']
