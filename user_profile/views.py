from django.shortcuts import render,redirect
from .forms import StudentProfileUpdateForm,TeacherProfileUpdateForm
from student.models import Student
from teacher.models import Teacher
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# Create your views here.
def user_profile(request):
    return render(request,'user_profile/user_profile.html')


def update_profile(request):
    # Check if the user has a student profile
    student = Student.objects.filter(user=request.user).first()
    teacher = Teacher.objects.filter(user=request.user).first()  # Check for teacher profile

    if student is not None:
        # Initialize form with the student's existing data
        form = StudentProfileUpdateForm(instance=student)

        if request.method == "POST":
            # Pass both POST data and FILES to the form
            form = StudentProfileUpdateForm(instance=student, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()  # Save the updated student profile with the image file
                return redirect("user_profile:user_profile")

    elif teacher is not None:
        # Initialize form with the teacher's existing data
        form = TeacherProfileUpdateForm(instance=teacher)

        if request.method == "POST":
            # Pass both POST data and FILES to the form
            form = TeacherProfileUpdateForm(instance=teacher, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()  # Save the updated teacher profile with the image file
                return redirect("user_profile:user_profile")

    # If the form is not valid, or if it's a GET request, render the form with errors
    return render(
        request,
        "user_profile/update_profile.html",
        context={
            "form": form,
        },
    )


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'user_profile/password_change.html'
    success_url = reverse_lazy('user_profile:user_profile')

    def form_valid(self, form):
        print("Your password was successfully updated!")
        return super().form_valid(form)