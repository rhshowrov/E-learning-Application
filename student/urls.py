from django.urls import path,include
from django.contrib import admin
from student import views
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns

app_name='student'

urlpatterns=[
  path('',views.stdHomePage,name='stdHomePage'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)