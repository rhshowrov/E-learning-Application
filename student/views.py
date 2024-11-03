from django.shortcuts import render
from student.models import Student
from teacher.models import TeacherEnrolled
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def stdHomePage(request,student_id):
  student=Student.objects.get(user=request.user)
  enrolled_courses=student.student_enrollments.all()
  course_data=[]
  for enrollment in enrolled_courses:
    course = enrollment.course  # Access the course instance 
    # Get course details
    course_name = course.name
    course_code = course.code
    course_section = course.section
    course_pic = course.course_pic
    course_id= course.id
    print(course_pic)
    # Get the teacher enrolled in this course
    try:
        course_instructor = TeacherEnrolled.objects.get(course=course).teacher.fullname
    except TeacherEnrolled.DoesNotExist:
        course_instructor = "No teacher assigned"
    
    # Append course and instructor details to the list
    course_data.append({
        'course_id': course_id,
        'course_name': course_name,
        'course_code': course_code,
        'course_section': course_section,
        'course_pic': course_pic,
        'course_instructor': course_instructor
    })
    
  return render(request,'stdbase.html',context={
    "student_id":student_id,
    'profile':student,
    'course':course_data,
  })