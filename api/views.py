from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializer import UserSerializer

# Create your views here.


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
