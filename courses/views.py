from django.shortcuts import render
from .models import CourseFile,Course,CourseAssignment
from django.shortcuts import get_object_or_404,HttpResponse,HttpResponseRedirect
from .forms import AssignmentUploadForm
from student.models import Student,StudentEnrolled
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
    'course':course,
    'course_files':course_files,
  })
  

def assignment(request, pk):
    # Retrieve the course using get_object_or_404
    course = get_object_or_404(Course, pk=pk)
    
    # Filter assignments by the course
    assignments = CourseAssignment.objects.filter(course=course)

    # Initialize form
    form = AssignmentUploadForm()

    if request.method == "POST":
        # Process the uploaded form data
        form = AssignmentUploadForm(data=request.POST, files=request.FILES)  # Include files
        if form.is_valid():
            assignment_id = request.POST.get('assignment_id')
            assignment = get_object_or_404(CourseAssignment, pk=assignment_id)

            # Get the student who is uploading
            student = get_object_or_404(Student, user=request.user)

            # Optionally, check if student is enrolled in the course (not implemented yet)

            # Save the uploaded file and link it with the assignment
            upload = form.save(commit=False)
            upload.assignment = assignment
            upload.student = student  # Assuming you have a student field in AssignmentUploadFile
            upload.upload_status = True  # Mark as uploaded
            upload.save()

        else:
            # If form is invalid, you can return errors to the template
            return render(request, 'course/assignment.html', {
                'course': course,
                'assignments': assignments,
                'form': form,
            })

    # Render the form in the template regardless of method
    return render(request, 'course/assignment.html', {
        'course': course,
        'assignments': assignments,
        'form': form,
    })

  