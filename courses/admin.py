from django.contrib import admin
from .models import Course,CourseQuiz,CourseFile,QuizAnswer,CourseAssignment,AssignmentUploadFile,QuizResult
# Register your models here.
admin.site.register(Course)
admin.site.register(CourseQuiz)
admin.site.register(CourseFile)
admin.site.register(QuizAnswer)
admin.site.register(CourseAssignment)
admin.site.register(AssignmentUploadFile)
admin.site.register(QuizResult)
