from .models import Student

def profile_context(request):
    # Ensure the user is authenticated before trying to get their profile
    if request.user.is_authenticated:
        try:
            student_profile = Student.objects.get(user=request.user)
            return {'profile': student_profile}
        except Student.DoesNotExist:
            return {}
    return {}
