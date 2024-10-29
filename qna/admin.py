from django.contrib import admin
from .models import QNA,QnaReply,QnaLike
# Register your models here.
admin.site.register(QNA)
admin.site.register(QnaReply)
admin.site.register(QnaLike)