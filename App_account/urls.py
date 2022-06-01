from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.userSign, name='signup'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
]