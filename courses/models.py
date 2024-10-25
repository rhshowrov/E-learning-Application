from django.db import models
# Create your models here.
class Course(models.Model):
  name=models.CharField(max_length=100,blank=False)
  code=models.CharField(max_length=10,blank=False)
  section=models.IntegerField()
  course_pic=models.ImageField(upload_to='course_thumbnail',blank=True)
  class Meta:
    unique_together=('name','code','section')
  def __str__(self):
        return f"{self.name} - {self.code} (Section: {self.section})"

class CourseFile(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_files')
    title = models.CharField(max_length=255,blank=False)
    file = models.FileField(upload_to='course_files/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"File: {self.file.name} uploaded on {self.date}"


class CourseQuiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=30)
    quiz_number=models.PositiveSmallIntegerField(default=0)
    total_marks = models.IntegerField()
    duration = models.PositiveIntegerField(blank=False)
    start_time = models.DateTimeField(blank=False)  # Field for the start time
    end_time = models.DateTimeField(blank=False)    # Field for the end time
    publish_status=models.BooleanField(default=False)

    def __str__(self):
        return f"Quiz: {self.quiz_number} for {self.course.name}"


class QuizAnswer(models.Model):
    quiz = models.ForeignKey(CourseQuiz, on_delete=models.CASCADE, related_name='answers')
    question_text = models.CharField(max_length=500)  # Added question text
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    correct_answer = models.IntegerField()  # Store the index of the correct option (1-4)
    question_mark=models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"Question: {self.question_text} for {self.quiz.title}"

class QuizResult(models.Model):
    quiz=models.ForeignKey(CourseQuiz,on_delete=models.CASCADE, related_name='quiz_results')
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='student_quiz_results',)
    obtained_marks=models.PositiveIntegerField(null=True)
    submit_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('quiz', 'student')
    def __str__(self):
        return f"{self.student} got {self.obtained_marks} in {self.quiz}"


class CourseAssignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignment')
    file = models.FileField(upload_to='course_files/assignments/', blank=True)
    assignment_text = models.TextField(default="No assignment Related text provided")
    assignment_number = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    
    # New fields
    due_date = models.DateTimeField()  # Add due date field
    total_marks = models.PositiveIntegerField(default=0)  # Total marks for the assignment

    def __str__(self):
        return f"Assignment for {self.course.code}.{self.course.section}"

      
class AssignmentUploadFile(models.Model):
    assignment = models.ForeignKey(CourseAssignment, on_delete=models.CASCADE, related_name='assignment_upload_file')
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='uploaded_assignment',null=True)
    
    file = models.FileField(upload_to='course_files/assignment_uploads/')
    date = models.DateField(auto_now_add=True)
    
    # New fields
    upload_status = models.BooleanField(default=False)  # Tracks whether the assignment is uploaded
    obtain_marks = models.PositiveIntegerField(default=0)  # Marks obtained for the assignment
    submit_date = models.DateTimeField(auto_now_add=True)  # Records submission date and time

    def __str__(self):
        return f"Assignment Uploaded by {self.student.student_id}"
