from django.urls import path,include
from user_handle import views
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
app_name='user_handle'
urlpatterns=[
  
  # path('signup/',views.create_user,name='signup'),
  path('',views.userLogin,name='userLogin'),
  # path('logout/',views.logout_user ,name='logout_user'),
  
  # path('edit-profile/',views.editprofile ,name='edit_profile'),
  
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)