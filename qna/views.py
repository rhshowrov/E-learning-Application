from django.shortcuts import render,get_object_or_404
from .models import QNA
# Create your views here.
def qna(request):      
  qnas=QNA.objects.all()
    
  context = {
        'qnas':qnas,
    }
  return render(request,'qna/qna.html',context=context)

def qna_details(request,slug):
      qna=get_object_or_404(QNA,qna_slug=slug)
      print(qna)
      context={
            'slug':slug,
            'q':qna,
      }
      return render(request,'qna/qna_details.html',context=context)