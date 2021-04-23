from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
        path('', views.home , name='courses_home'),
        path('tracks/', views.tracks , name='tracks'),
        

        path('details/<slug:slug>', views.details, name="course_details"),


]
