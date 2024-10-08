from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from courses.models import Course
from django.core.exceptions import ValidationError


# Create your models here.
class Teacher(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='teacher_profile')
  teacher_id=models.IntegerField(
        unique=True,
        validators=[MinValueValidator(10000), MaxValueValidator(99999)],  # Ensure it's a 5-digit number
        blank=True
  )
  fullname = models.CharField(max_length=120, blank=True)
  dob = models.DateField(blank=True,null=True)
  profile_pic = models.ImageField(upload_to='profile_pics/teacher', blank=True)
  profile_type = models.CharField(max_length=20, default="Teacher")
  def clean(self):
        if hasattr(self.user, 'student_profile'):
            raise ValidationError("This user is already assigned as a student.")
        super().clean()
  def __str__(self):
      return self.user.username
    
    
class TeacherEnrolled(models.Model):
  course=models.ForeignKey(Course,on_delete=models.CASCADE)
  teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE, related_name='teacher_enrollments')
  
  class Meta:
    unique_together=('course','teacher')
  def __str__(self):
    return f"teacher: {self.teacher} enrolled in {self.course}"