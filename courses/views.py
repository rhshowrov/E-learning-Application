from django.shortcuts import render
from .models import CourseFile,Course,CourseAssignment,CourseQuiz,QuizAnswer,QuizResult
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