from django.urls import path
from user_handle import views

app_name='user_handle'
urlpatterns=[
  
  # path('signup/',views.create_user,name='signup'),
  path('',views.userLogin,name='userLogin'),
  # path('logout/',views.logout_user ,name='logout_user'),
  # path('profile/',views.userProfile ,name='profile'),
  # path('edit-profile/',views.editprofile ,name='edit_profile'),
  
]