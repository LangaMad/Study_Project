
from django.views.generic import (
    FormView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    ListView,)
from django.contrib.auth import login,authenticate,logout
from  django.http import HttpResponse
from django.urls import reverse_lazy
from .form import LoginForm, UserRegisterForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# Create your views here.




class IndexPage(TemplateView):
    template_name = "index.html"


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data['username']
        phone = data['phone']
        password = data['password']
        user = authenticate(username=username , phone=phone, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponse('Ваш аккаунт неактивен')
        return HttpResponse('Такого юзера не существует')

class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')



def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')



class StudentListView(ListView):
    model = Student
    template_name = 'teacher_room.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    template_name = 'create_student.html'
    fields = ['name', 'email', 'birth_date', 'grade', 'address', 'gender']
    success_url = '/students/'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'update_student.html'
    fields = ['name', 'email', 'birth_date', 'grade', 'address', 'gender']
    success_url = '/students/'


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'delete_student.html'
    success_url = '/students/'


class StudentDetailView(DeleteView):
    model = Student
    template_name = 'view_student.html'
    context_object_name = 'student'





