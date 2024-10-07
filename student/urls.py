from django.urls import path,include
from django.contrib import admin
from student import views

app_name='student'

urlpatterns=[
  path('',views.stdHomePage,name='stdHomePage'),
]