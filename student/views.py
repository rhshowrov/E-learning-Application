from django.shortcuts import render
from student.models import Student
# Create your views here.
def stdHomePage(request,student_id):
  
  student=Student.objects.get(user=request.user)
  course=student.student_enrollments.all()
  print(course[0].student)
  return render(request,'stdbase.html',context={
    "student_id":student_id,
    'profile':student,
    'course':course,
  })