from django import forms
from qna.models import QNA

class CreateQnaForm(forms.ModelForm):
  class Meta:
    model=QNA
    fields=['title','qna_text','qna_img']
    
    
  