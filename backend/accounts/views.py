from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer

class User(generics.CreateAPIView):
    serializer_class = UserSerializer
