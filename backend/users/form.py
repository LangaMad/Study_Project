from django import forms
from .models import Teacher, Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



class UserRegisterForm(UserCreationForm):

    class Meta:

        model = Teacher
        fields = [
            'username',
            'email',
            'phone',
            'teacher_subject',


        ]

        widgets = {
            "teacher_subject": forms.TextInput(attrs={"class": "registration-form","placeholder":"Предмет"}),
            "phone": forms.TextInput(attrs={"class": "registration-form","placeholder":"Номер телефона"}),
            "email": forms.EmailInput(attrs={"class": "registration-form", "placeholder": "Email"}),
            "username": forms.TextInput(attrs={"class": "registration-form", "placeholder": "ФИО"}),

        }


class LoginForm(AuthenticationForm):

    phone = forms.CharField(max_length=10)

    class Meta:
        fields = ['username', 'phone', 'password']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'birth_date', 'grade', 'address', 'gender']
