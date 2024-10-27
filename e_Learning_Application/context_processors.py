from student.models import Student
from teacher.models import Teacher

from student.models import Student
from teacher.models import Teacher

def profile_context(request):
    context = {
        'profile': None,
        'is_student': False,
        'is_teacher': False,
        'base_template': "default.html"  # Default template if unauthenticated or no profile
    }
    
    # Only proceed if user is authenticated
    if request.user.is_authenticated:
        # Check if the user has a Student profile
        student_profile = getattr(request.user, 'student_profile', None)
        teacher_profile = getattr(request.user, 'teacher_profile', None)
        
        if student_profile:
            context.update({
                'profile': student_profile,
                'is_student': True,
                'id': student_profile.student_id,
                'base_template': "stdbase.html"
            })
        elif teacher_profile:
            context.update({
                'profile': teacher_profile,
                'is_teacher': True,
                'id': teacher_profile.teacher_id,
                'base_template': "tchbase.html"
            })
    
    return context

