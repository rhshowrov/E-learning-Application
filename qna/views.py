from django.shortcuts import render

# Create your views here.
def qna(request):
  if hasattr(request.user.student_profile, 'student_id'):
        base_template = "stdbase.html"
  else:
        base_template = "tchbase.html"
    
  context = {
        'base_template': base_template,
    }
  return render(request,'qna/qna.html',context=context)