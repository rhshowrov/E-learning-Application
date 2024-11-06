from django.shortcuts import render,redirect
from .models import CourseFile,Course,CourseAssignment,CourseQuiz,QuizAnswer,QuizResult
from django.shortcuts import get_object_or_404,HttpResponse,HttpResponseRedirect
from .forms import AssignmentUploadForm,UploadMaterialForm,CourseAssignmentForm
from student.models import Student,StudentEnrolled
from teacher.models import Teacher,TeacherEnrolled
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

@login_required
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
  
@login_required
def assignment(request, pk):
    # Retrieve the course using get_object_or_404
    course = get_object_or_404(Course, pk=pk)
    
    # Filter assignments by the course
    assignments = CourseAssignment.objects.filter(course=course)
    is_student = hasattr(request.user, 'student_profile')
    is_teacher = hasattr(request.user, 'teacher_profile')
    if is_student:
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
                upload.student = student  
                upload.upload_status = True  # Mark as uploaded
                upload.save()
                return redirect('assignment', pk=pk)

            else:
                # If form is invalid, you can return errors to the template
                return render(request, 'course/assignment.html', {
                    'course': course,
                    'assignments': assignments,
                    'form': form,
                })
    if is_teacher:
        return render(request, 'course/assignment.html', {
                    'course': course,
                    'assignments': assignments,
                })
        
    # Render the form in the template regardless of method
    return render(request, 'course/assignment.html', {
        'course': course,
        'assignments': assignments,
        'form': form if is_student else None,
    })

@login_required
def quizes(request,pk):
    course=get_object_or_404(Course,pk=pk)
    quizes = CourseQuiz.objects.filter(course=course)
    student=get_object_or_404(Student,user=request.user)
    submitted_quizes = []
    for quiz in quizes:
        # Check if the student has already submitted this specific quiz
        if QuizResult.objects.filter(quiz=quiz, student=student).exists():
            submitted_quizes.append(quiz.pk)
    print(submitted_quizes)
    context={
        "quizes":quizes,
        "course":course,
        'submitted_quizes': submitted_quizes,
    }
    return render(request,'course/quizes.html',context=context)


@login_required
def take_quiz(request,pk):
    quiz=get_object_or_404(CourseQuiz,pk=pk)
    course=quiz.course
    quiz_question=QuizAnswer.objects.filter(quiz=quiz)
    context={
        'quiz':quiz,
        'course':course,
        'question':quiz_question
    }
    return render(request,'course/take_quiz.html',context=context)



@login_required
def quiz_result(request,pk):
    quiz=get_object_or_404(CourseQuiz,pk=pk)
    course=quiz.course
    quiz_question=QuizAnswer.objects.filter(quiz=quiz)
    total_score=0

    #generating Quiz result
    if request.method=="POST":
        for q in quiz_question:
           user_answer=request.POST.get(f'question_{q.id}')
           if user_answer:
               user_answer=int(user_answer)
               if user_answer==q.correct_answer:
                   total_score+= q.question_mark
    # Create a new QuizResult object for this student
    QuizResult.objects.create(
        quiz=quiz,
        student=get_object_or_404(Student,user=request.user),
        obtained_marks=total_score
    )

    # Print the student's total score (for debugging)
    print(f"The student's total score is: {total_score}")               
    context={
        'quiz':quiz,
        'course':course,
        'question':quiz_question,
        'score':total_score,
    }
    return render(request,'course/quiz_result.html',context=context)

@login_required
def people(request,pk):
    course=get_object_or_404(Course,pk=pk)
    #getting assigned teacher
    teacher_obj = TeacherEnrolled.objects.filter(course=course).first()
    if teacher_obj is not None:
      teacher=teacher_obj.teacher
    else:
        teacher=False
    #getting all Student who are enrolled in a course
    students=StudentEnrolled.objects.filter(course=course)
    context={
        'teacher':teacher,
        'students':students,
        'course':course,
    }
    return render(request,'course/people.html',context=context)


def upload_content(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = UploadMaterialForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        temp = form.save(commit=False)
        temp.course = course
        temp.save()
        url = reverse('courses:courseContent', kwargs={'pk': pk})
        return HttpResponseRedirect(url)

    return render(request, 'course/upload_content.html',context={
        'form': form,
        'course':course,
        })
    
    
def createAssignment(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseAssignmentForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        temp = form.save(commit=False)
        temp.course = course
        temp.save()
        return HttpResponseRedirect(reverse('courses:assignment', kwargs={'pk': pk}))

    # Render form if GET request or form is invalid
    return render(request, 'course/create_assignment.html', context={
        'form': form,
        'course':course,
    })   
            
            