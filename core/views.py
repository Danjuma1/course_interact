from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime

from .forms import MessageForm, NotificationForm
from .models import Notification, Message
from accounts.models import Lecturer, Student, Course


def index(request):
    return render(request, 'core/index.html')

@login_required
def student_main(request):
    student = Student.objects.get(user=request.user)
    courses = student.course_list.all()
    notifications = Notification.objects.filter(course__in=courses)
    return render(request, 'core/student_main.html', {'courses': courses, 'notifications': notifications})

@login_required
def student_detail(request, course_id):
    user = request.user
    student = Student.objects.get(user=request.user)
    courses = student.course_list.all()
    course = Course.objects.get(id=course_id)
    lecturer = course.lecturer
    messages = Message.objects.filter(course=course)
    form = MessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            message = form.save(commit=False)
            message.course = course
            message.sender = user
            message.save()
            try:
                student = Student.objects.get(user=request.user)
                return redirect('student_detail', course_id)

            except:
                return redirect('lecturer_detail', course.id)

    else:
        form = MessageForm()

        context = {
            'course': course,
            'user': user,
            'lecturer': lecturer,
            'student': student,
            'courses': courses,
            'messages': messages,
            'form': form
        }

        return render(request, 'core/student_detail.html', context)


@login_required
def lecturer_main(request):
    user = request.user
    lecturer = Lecturer.objects.get(user=request.user)
    courses = Course.objects.filter(lecturer=lecturer)
    context = {
        'user': user,
        'lecturer': lecturer,
        'courses': courses,
    }
    return render(request, 'core/lecturer_main.html', context)


@login_required
def lecturer_detail(request, course_id):
    user = request.user
    lecturer = Lecturer.objects.get(user=request.user)
    courses = Course.objects.filter(lecturer=lecturer)
    course = Course.objects.get(id=course_id)
    messages = Message.objects.filter(course=course)
    form = MessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            message = form.save(commit=False)
            message.course = course
            message.sender = user
            message.save()
            try:
                student = Student.objects.get(user=request.user)
                return redirect('core:student_detail', course_id)

            except:
                return redirect('core:lecturer_detail', course.id)

    else:
        form = MessageForm()

        context = {
                'user': user,
                'lecturer': lecturer,
                'course': course,
                'courses': courses,
                'messages': messages,
                'form' : form
            }

        return render(request, 'core/lecturer_detail.html', context)


@login_required
def add_notification(request, course_id):
    form = NotificationForm(request.POST or None)
    course = Course.objects.get(id=course_id)
    if form.is_valid():
        notification = form.save(commit=False)
        notification.course = course
        notification.save()
        return redirect('lecturer_detail', course.id)

    return render(request, 'core/add_notification.html', {'course': course, 'form': form})


