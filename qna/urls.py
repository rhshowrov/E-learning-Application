from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from qna import views
app_name='qna'
urlpatterns = [
    path('', views.qna,name='qna'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)