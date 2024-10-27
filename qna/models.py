from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

class QNA(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qna')
    title = models.CharField(max_length=200, blank=False)
    qna_text = models.TextField(blank=False)
    qna_img = models.ImageField(blank=True)
    qna_slug = models.SlugField(max_length=264, unique=True, blank=True)  # Slug field
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def save(self, *args, **kwargs):
        if not self.qna_slug:  # Only create a slug if it doesn't already exist
            base_slug = slugify(self.title)  # Create a base slug from the title
            unique_suffix = str(uuid.uuid4())[:8]  # Generate a unique suffix (first 8 chars of UUID)
            self.qna_slug = f"{base_slug}-{unique_suffix}"  # Append UUID to the slug
        super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        return self.title

      
