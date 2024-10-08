from django.shortcuts import render
from student.models import Student
# Create your views here.
def stdHomePage(request,student_id):
  
  student=Student.objects.get(user=request.user)
  print(f'Phtoo: {student.profile_pic}')
  return render(request,'stdbase.html',context={
    "student_id":student_id,
    'profile':student,
  })