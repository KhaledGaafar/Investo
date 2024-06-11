from django.shortcuts import render
from rest_framework import generics
from .models import Articles,Courses,Videos
from .serializers import ArticlesSerializer,VideosSerializer,CoursesSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ArticlesView(generics.ListCreateAPIView):
    #permission_classes=[IsAuthenticated]
    queryset=Articles.objects.all()
    serializer_class=ArticlesSerializer
    search_fields=['level']

class Articleupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticlesSerializer



class VideosView(generics.ListCreateAPIView):
    #permission_classes=[IsAuthenticated]
    queryset=Videos.objects.all()
    serializer_class=VideosSerializer
    search_fields=['level']

class Viedeosupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=Videos.objects.all()
    serializer_class=VideosSerializer

class CoursesView(generics.ListCreateAPIView):
   # permission_classes=[IsAuthenticated]
    queryset=Courses.objects.all()
    serializer_class=CoursesSerializer
    search_fields=['level']

class Coursesupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=Courses.objects.all()
    serializer_class=CoursesSerializer



