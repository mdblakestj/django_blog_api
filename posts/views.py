# api/views.py
from rest_framework import generics

from posts.models import Post
from .serializers import PostSerializer


class ListPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
