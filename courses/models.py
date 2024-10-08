from django.db import models

# Create your models here.
class Course(models.Model):
  name=models.CharField(max_length=100,blank=False)
  code=models.CharField(max_length=10,blank=False)
  section=models.IntegerField(unique=True)
  def __str__(self):
        return f"{self.name} - {self.code} (Section: {self.section})"
