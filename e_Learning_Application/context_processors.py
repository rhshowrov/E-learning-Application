from student.models import Student
from teacher.models import Teacher

def profile_context(request):
    # Ensure the user is authenticated before trying to get their profile
    if request.user.is_authenticated:
        # First, try to get the student's profile
        try:
            student_profile = Student.objects.get(user=request.user)
            return {'profile': student_profile, 'is_student': True, 'is_teacher': False,'id':student_profile.student_id}
        except Student.DoesNotExist:
            pass  # If the student profile does not exist, proceed to check for teacher

        # Next, try to get the teacher's profile
        try:
            teacher_profile = Teacher.objects.get(user=request.user)
            return {'profile': teacher_profile, 'is_student': False, 'is_teacher': True,'id':teacher_profile.teacher_id}
        except Teacher.DoesNotExist:
            pass  # If neither profile exists, an empty context will be returned

    # If the user is not authenticated or has no profile, return an empty context
    return {'profile': None, 'is_student': False, 'is_teacher': False}
