from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
#one to one model with userprofile
class Student(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='student')
  # Custom ID field for admin-assigned 5-digit integer
  student_id = models.IntegerField(
        unique=True,
        validators=[MinValueValidator(10000), MaxValueValidator(99999)],  # Ensure it's a 5-digit number
        blank=True
    )
  
  fullname = models.CharField(max_length=120, blank=True)
  dob = models.DateField(blank=True,null=True)
  profile_pic = models.ImageField(upload_to='profile_pics/students', blank=True)
  profile_type = models.CharField(max_length=20, default="Student")

  def __str__(self):
      return self.user.username