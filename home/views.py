from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Post
from .serializers import *

class Index(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = IndexSerializer
    
