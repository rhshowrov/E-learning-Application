from django import forms
from courses.models import AssignmentUploadFile

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
        
  