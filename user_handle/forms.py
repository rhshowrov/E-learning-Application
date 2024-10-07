from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class userLoginForm(AuthenticationForm):
  models=User
  fields=['username','password']
  widgets={
    "username":forms.TextInput(attrs=({'class':'form_input','placeholder':"username"})),
    "password":forms.PasswordInput(attrs=({'class':'form_input','placeholder':"password"}))
  }
  labels={
    'username':"Enter Your Username:",
    "password":"Enter Your Password:",
  }

