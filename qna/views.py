from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect
from .models import QNA,QnaReply,QnaLike
from django.db.models import Q
# Create your views here.
from django.db.models import Q
from django.shortcuts import render
from .models import QNA
from django.urls import reverse
from qna.forms import CreateQnaForm
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def qna_details(request, slug):
    qna = get_object_or_404(QNA, qna_slug=slug)
    
    if request.method == "POST":
        reply_text = request.POST.get('reply_text')
        
        # Ensure reply_text exists and is not empty
        if reply_text:
            QnaReply.objects.create(
                user=request.user,
                qna_object=qna,
                reply_text=reply_text.strip()
            )
        # Redirect to avoid duplicate submissions on refresh
        return redirect('qna:qna_details', slug=slug)
    
    # GET request handling
    replies = QnaReply.objects.filter(qna_object=qna)
    context = {
        'slug': slug,
        'replies': replies,
        'q': qna,
    }
    return render(request, 'qna/qna_details.html', context=context)



@login_required
def createQna(request):
    if request.method == "POST":
        form = CreateQnaForm(data=request.POST)
        if form.is_valid():
            qna=form.save(commit=False)
            author=request.user
            qna.author=author
            qna.qna_img = request.FILES['qna_img']
            qna.save()
            return redirect(reverse('qna:qna'))
    else:
        form = CreateQnaForm()

    return render(request, 'qna/createqna.html', {'form': form})
        









def liked(request, pk):
    # Fetch the QNA object
    qna = get_object_or_404(QNA, pk=pk)
    
    # Check if the user has already liked this QNA using QnaLike
    like = QnaLike.objects.filter(qna=qna, user=request.user).first()

    if like:
        # If the like exists, delete it to "unlike"
        like.delete()
    else:
        # If it doesn't exist, create a new like
        QnaLike.objects.create(qna=qna, user=request.user)

    # Redirect to the QNA detail view
    return HttpResponseRedirect(reverse('qna:qna'))


        