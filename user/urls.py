from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('signup/', views.signup , name='signup'),
    path('login/', views.login_fn , name='login'),
    path('logout/', views.logout_fn , name='logout'),
    path('contact/', views.contact , name='contact'),

]
