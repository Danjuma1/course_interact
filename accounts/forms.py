from django import forms
from django.contrib.auth.models import User
from .models import Student, Lecturer

class UserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class StudentRegistration(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'matric_no', 'course_list']


