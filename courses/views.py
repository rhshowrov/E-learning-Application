from django.shortcuts import render

# Create your views here.
def courseContent(request,pk):
  
  return render(request,'course/courseDetails.html',context={
    'pk':pk,
  })
  