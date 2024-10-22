from django.urls import path,include
from django.contrib import admin
from courses import views
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns

app_name='courses'

urlpatterns=[
  path('',views.courseContent,name='courseContent'),
  path('assignments/',views.assignment,name="assignment"),
  path('quizes/',views.quizes,name="quizes"),
  
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)