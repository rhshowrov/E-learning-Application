from django.shortcuts import render
from teacher.models import Teacher,TeacherEnrolled
# Create your views here.
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
    # Append course and instructor details to the list
    course_data.append({
        'course_name': course_name,
        'course_code': course_code,
        'course_section': course_section,
        'course_pic': course_pic,
    })
    print(course_data)
    return render(request,'stdbase.html',context={
    "teacher_id":teacher_id,
    'profile':teacher,
    'course':course_data,
  })