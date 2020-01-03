from django.shortcuts import render
from .serializer import PostSerializer
from rest_framework.viewsets import ModelViewSet
from users.models import Post
# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('id')[:10]
    serializer_class = PostSerializer
