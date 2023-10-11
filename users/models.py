from django.db import models

from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)

    def __str__(self):
        return str(self.name)

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name=user.username,
        )

post_save.connect(createProfile, sender=User)

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                 related_name="user_follower")
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                 related_name="user_followed")

    created = models.DateTimeField(auto_now_add=True, null=True)