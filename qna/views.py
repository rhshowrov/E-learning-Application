from django.shortcuts import render,get_object_or_404
from .models import QNA,QnaReply
from django.db.models import Q
# Create your views here.
from django.db.models import Q
from django.shortcuts import render
from .models import QNA

def qna(request):
    # Check if the request method is GET
    if request.method == "GET":
        query = request.GET.get('q')
        if query:
            # If there's a search query, filter QNAs based on the query
            qnas = QNA.objects.filter(
                Q(title__icontains=query) |
                Q(qna_text__icontains=query)
            )
        else:
            # If no query, retrieve all QNAs
            qnas = QNA.objects.all()
        
        # Context for rendering the template
        context = {
            'qnas': qnas,
        }
        return render(request, 'qna/qna.html', context=context)


def qna_details(request,slug):
      qna=get_object_or_404(QNA,qna_slug=slug)
      replies=QnaReply.objects.filter(qna_object=qna)
      context={
            'slug':slug,
            'replies':replies,
            'q':qna,
      }
      return render(request,'qna/qna_details.html',context=context)