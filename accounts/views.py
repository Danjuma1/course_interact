from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import UserRegistration, StudentRegistration
from .models import Student, User, Lecturer


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            try:
                student = Student.objects.get(user=request.user)
                return redirect('core:student_main')
            except:
                return redirect('core:lecturer_main')
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'accounts/login.html')



def register_user(request):
    user_form = UserRegistration(request.POST or None)
    student_form = StudentRegistration(request.POST or None)

    if user_form.is_valid() and student_form.is_valid():
        user = user_form.save(commit=False)
        username = user_form.cleaned_data['username']
        password = user_form.cleaned_data['password']
        user.set_password(password)
        user.save()

        student = student_form.save(commit=False)
        student.user = User.objects.get(id=user.id)
        student.save()
        student_form.save_m2m() # saves the many to many field relation (between the course and student model) entered in the form while selecting the courses

        return login_user(request)

    return render(request,'accounts/register_user.html', {'user_form': user_form, 'student_form': student_form})


def logout_user(request):
    logout(request)
    return render(request, 'login.html')


