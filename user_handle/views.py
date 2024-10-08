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
        if hasattr(user, 'student'):
          login(request,user)
          student_id=user.student.student_id
          return HttpResponseRedirect(reverse('student:stdHomePage',kwargs={'student_id': student_id}))
        if hasattr(user, 'teacher'):
          login(request,user)
          return HttpResponse("<h1>Your are a Teacher </h1>")
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


 

    