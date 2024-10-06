from django.shortcuts import render,HttpResponse
from .forms import userLoginForm
from django.contrib.auth import authenticate, login, logout
# Messages
from django.contrib import messages

# Create your views here.
def userLogin(request):
  form=userLoginForm()
  if request.method=="POST":
    form=userLoginForm(data=request.POST)
    if form.is_valid():
      username=form.cleaned_data.get("username")
      password=form.cleaned_data.get("password")
      user=authenticate(username=username, password=password)
      if user is not None:
        if user.user_profile.profile_type =="Student":
          login(request,user)
          return HttpResponse("<h1>Your are s Student </h1>")
        elif user.user_profile.profile_type =="Teacher":
          login(request,user)
          return HttpResponse("<h1>Your are a Teacher </h1>")
        else:
          return HttpResponse("<h1>Your are Unauthorized </h1>")
      else:
        # Authentication failed, display error
        messages.error(request, "Invalid username or password.")
    else:
      messages.error(request, "Invalid Input")
      return HttpResponse("<h1>Invalid Inputk</h1>")
        
  else:
    return render(request,'user_handle/userlogin.html',context={'form':form})     
  
  