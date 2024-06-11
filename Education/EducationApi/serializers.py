from rest_framework import serializers
from .models import Articles,Videos,Courses


class ArticlesSerializer(serializers.ModelSerializer):

    class Meta:
        model=Articles
        fields=['level','title','description','date','image']



class VideosSerializer(serializers.ModelSerializer):

    class Meta:
        model=Videos
        fields=['level','title','author','author_image','date','video']


class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model=Courses
        fields=['level','title','author','image','link']