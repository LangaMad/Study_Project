from django import forms
from .models import Teacher
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))
    class Meta:
        model = Teacher
        fields = [
            'teacher_subject',
            'phone',

        ]

        widgets = {
            "teacher_subject": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),

        }


class LoginForm(forms.Form):
    phone = forms.CharField(
        label="Номер",
        widget=forms.TextInput(attrs={"class":"form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "type":"password",
                "autocomplete":"off",
                "placeholder":"Пароль"
            }
            )
    )

