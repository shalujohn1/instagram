from rest_framework import serializers
from instaprojects.models import Post
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    profile =serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = '__all__'

    def get_profile(self, obj):
        profile = Profile.objects.get(user=obj.owner)
        serializer = ProfileSerializer(profile, many=False)
        return serializer.data