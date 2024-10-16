from django.shortcuts import render
from .models import CourseFile,Course
from django.shortcuts import get_object_or_404
# Create your views here.
def courseContent(request,pk):
  course=get_object_or_404(Course, pk=pk)
  print(course)
  course_files = CourseFile.objects.filter(course=course).order_by("date")
  print(course_files)
  # Check file type and add 'is_pdf' or 'is_pptx' flag
  for file in course_files:
      file.is_pdf = file.file.url.lower().endswith('.pdf')
      file.is_pptx = file.file.url.lower().endswith('.pptx')
  return render(request,'course/courseDetails.html',context={
    'pk':pk,
    'course_files':course_files,
  })
  

  