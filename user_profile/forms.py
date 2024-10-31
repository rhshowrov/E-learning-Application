from django import forms
from student.models import Student
from teacher.models import Teacher

class StudentProfileUpdateForm(forms.ModelForm):
  class Meta:
      model=Student
      fields=['fullname','profile_pic']

class TeacherProfileUpdateForm(forms.ModelForm):
  class Meta:
        model=Teacher
        fields=['fullname','profile_pic']
  