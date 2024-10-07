from django.shortcuts import render

# Create your views here.
def stdHomePage(request,custom_id):
  return render(request,'stdbase.html',context={
    "custom_id":custom_id,
  })