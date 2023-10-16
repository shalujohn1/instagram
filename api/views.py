from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer, ProfileSerializer
from instaprojects.models import Post
from users.models import Profile
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()



class postListView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin
                   ):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class postdetailview(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get(self, request, id):
        return self.retrieve(request, id)

    def put(self, request, id):
        return self.update(request, id)
    def delete(self, request, id):
        return self.destroy(request, id)


class postListView(APIView):
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        owner_id = data["owner"]
        owner = User.objects.get(id=owner_id)

        add_post = Post.objects.create(

            description=request.data['description'],

            owner=owner,

        )
        serializer = PostSerializer(add_post, many=False)
        return Response(serializer.data, status=201)


class postdetailview(APIView):
    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist as e:
            return Response({"error": "given post object not fund"}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serializer = PostSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = PostSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        instance = self.get_object(id)

        instance.delete()
        return Response("successfully deleted", status=status.HTTP_204_NO_CONTENT)
