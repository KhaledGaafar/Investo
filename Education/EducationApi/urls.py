from django.urls import path
from . import views

urlpatterns =[
    path("articles/",views.ArticlesView.as_view()),
    path("articlesupdate/<int:pk>",views.Articleupdate.as_view()),
    path("courses/",views.CoursesView.as_view()),
    path("coursesupdate/<int:pk>",views.Coursesupdate.as_view()),
    path("videos/",views.VideosView.as_view()),
    path("videosupdate/<int:pk>",views.Viedeosupdate.as_view()),


]