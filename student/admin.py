from django.contrib import admin
from .models import Student,StudentEnrolled
# Register your models here.
admin.site.register(Student)
admin.site.register(StudentEnrolled)