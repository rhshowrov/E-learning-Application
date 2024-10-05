from django.db import models
from django.contrib.auth import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class UserProfile(models.Model):
    class ProfileType(models.TextChoices):
        TEACHER = 'Teacher', 'Teacher'
        STUDENT = 'Student', 'Student'

    # Custom ID field for admin-assigned 5-digit integer
    custom_id = models.IntegerField(
        unique=True,
        validators=[MinValueValidator(10000), MaxValueValidator(99999)],  # Ensure it's a 5-digit number
        blank=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    fullname = models.CharField(max_length=120, blank=True)
    dob = models.DateField()
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    profile_type = models.CharField(max_length=7, choices=ProfileType.choices, default=ProfileType.STUDENT)

    def __str__(self):
        return self.user.username
  