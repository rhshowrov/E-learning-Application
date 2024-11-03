from django.shortcuts import render
from teacher.models import Teacher,TeacherEnrolled
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def tchHomePage(request,teacher_id):
  teacher=Teacher.objects.get(user=request.user)
  enrolled_courses=teacher.teacher_enrollments.all()
  course_data=[]
  for enrollment in enrolled_courses:
    course = enrollment.course  # Access the course instance 
    # Get course details
    course_name = course.name
    course_code = course.code
    course_section = course.section
    course_pic = course.course_pic
    course_id= course.id
    # Append course and instructor details to the list
    course_data.append({
        'course_name': course_name,
        'course_code': course_code,
        'course_section': course_section,
        'course_pic': course_pic,
        'course_id': course_id,
    })
    print('Teacher Home accessed!')
    print(course_data)
    return render(request,'tchbase.html',context={
    "teacher_id":teacher_id,
    'profile':teacher,
    'course':course_data,
  })