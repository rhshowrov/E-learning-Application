from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class QNA(models.Model):
  author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='qna')
  title=models.CharField(max_length=200,blank=False)
  qna_text=models.TextField(blank=False)
  qna_img=models.ImageField(blank=True)
  qna_slug=models.SlugField(max_length=264, unique=True)
  publish_date=models.DateTimeField(auto_now_add=True)
  update_date=models.DateTimeField(auto_now=True)
  class Meta:
        ordering = ['-publish_date']
  def __str__(self):
        return self.title
      
