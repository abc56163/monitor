from django.urls import path, include, reverse
from django.shortcuts import redirect
from django.contrib import admin
from thmonitor import views
urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.login),
    path('index/', views.index),
    path('regist/', views.regist),
    path('login/', views.login),
    path('loginout/', views.loginout),
    path('user/', views.user, name='user'),
    path('form/', views.form, name='form'),
    path('main/', views.main, name='main'),


]
