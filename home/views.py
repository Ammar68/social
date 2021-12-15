from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response 
from .models import Post
from .serializers import *

class Index(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = IndexSerializer
    
  def post(self, request):
    return Response({"Posts" : self.queryset.values()})
  