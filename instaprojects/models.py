from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
import uuid


class Post(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(
        null=True, blank=True, default='')
    video = models.FileField(
        upload_to='videos/', null=True, blank=True)
    like = models.IntegerField(default=0)

    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)

    def __str__(self):
        return str(self.description)


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,
                             related_name="user_like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="post_like")
    created = models.DateTimeField(auto_now_add=True, null=True)

class Comment(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,
                             related_name="user_comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="post_comment")
    comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)







