from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('post_blog',views.post_blog,name='post_blog'),
    path('like_blog',views.like_blog,name='like_blog'),




]
