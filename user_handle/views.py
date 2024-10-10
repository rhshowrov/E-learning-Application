from django.shortcuts import render,HttpResponse,HttpResponseRedirect, get_object_or_404
from .forms import userLoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
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
        if hasattr(user, 'student_profile'):
          login(request,user)
          student_id=user.student_profile.student_id
          return HttpResponseRedirect(reverse('student:stdHomePage',kwargs={'student_id': student_id}))
        if hasattr(user, 'teacher_profile'):
          login(request,user)
          teacher_id=user.teacher_profile.teacher_id
          return HttpResponseRedirect(reverse('teacher:tchHomePage',kwargs={'teacher_id': teacher_id}))
        else:
          return HttpResponse("<h1>Your are Unauthorized </h1>")
      else:
        # Authentication failed, display error
        messages.error(request, "Invalid username or password.")
    else:
      messages.error(request, "Invalid Input")
      return HttpResponse("<h1>Invalid Input</h1>")
        
  else:
    return render(request,'user_handle/userlogin.html',context={'form':form})     

def userLogout(request):
  logout(request)
  return HttpResponseRedirect(reverse('user_handle:userLogin'))
 

    