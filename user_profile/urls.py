from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from user_profile import views

app_name='user_profile'
urlpatterns = [
    path('', views.user_profile,name='user_profile'),
    path('profile_update/',views.update_profile,name='update_profile'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)