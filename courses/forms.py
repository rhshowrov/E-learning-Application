from django import forms
from courses.models import AssignmentUploadFile,CourseFile,CourseAssignment

class AssignmentUploadForm(forms.ModelForm):
    class Meta:
        model = AssignmentUploadFile
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={
                'class': ' w-full ml-10 text-sm cursor-pointer  focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 my-1 ',
                'style': 'font-size: 14px;'
            }),
        }
        
class UploadMaterialForm(forms.ModelForm):
    class Meta:
        model=CourseFile
        fields=['title','file']


class CourseAssignmentForm(forms.ModelForm):
    class Meta:
        model=CourseAssignment
        fields=['assignment_text','assignment_number','due_date', 'total_marks','file']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'w-full p-3 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Select due date and time',
            }),
        }