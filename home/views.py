from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Post
from .serializers import *

class Index(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = IndexSerializer
  