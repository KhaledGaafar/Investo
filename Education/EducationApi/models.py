from django.db import models

# Create your models here.

class Articles(models.Model):
    level=models.CharField(max_length=50,default="begineers")
    title=models.CharField(max_length=255)
    description=models.TextField()
    date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='images')

class Videos(models.Model):
    level=models.CharField(max_length=50,default="begineers")
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=100)
    author_image=models.ImageField(upload_to='images')
    date=models.DateField(auto_now=True)
    video=models.FileField(upload_to='videos')

class Courses(models.Model):
    level=models.CharField(max_length=50,default='begineers')
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images',default='pngwing.com.png')
    link=models.URLField(default='https://www.coursera.org/learn/python-for-applied-data-science-ai')
