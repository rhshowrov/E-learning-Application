from django import template
from qna.models import QnaLike
register = template.Library()

@register.filter(name='is_liked')
def is_liked(qna, user):
    if user.is_authenticated:
        # Check if there is a like for the specific QnA by the user
        return QnaLike.objects.filter(qna=qna, user=user).exists()
    return False  # If the user is not authenticated, return False