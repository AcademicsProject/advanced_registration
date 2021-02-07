from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
        path('', views.home , name='courses_home'),

        path('<str:slug>', views.details, name="details"),

]
