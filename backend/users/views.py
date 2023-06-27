from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
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
from .form import LoginForm, UserRegisterForm, EmailForm
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
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return Student.objects.filter(Q(name__icontains=query))
        else:
            return Student.objects.all()


class StudentCreateView(CreateView):
    model = Student
    template_name = 'create_student.html'
    fields = ['name', 'father_name', 'surname', 'email', 'birth_d', 'gender', 'student_class', 'address']
    success_url = '/students/'

    def form_valid(self, form):
        response = super().form_valid(form)

        student = form.save()
        subject = 'Добро пожаловать в нашу школу!'
        message = f'Здравствуйте, {student.name}!\n\nВы успешно зарегистрированы в нашей школе.'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [student.email])
        return response


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'update_student.html'
    fields = ['name', 'father_name', 'surname', 'email', 'birth_d', 'gender', 'student_class', 'address']
    success_url = '/students/'

    def form_valid(self, form):
        response = super().form_valid(form)

        student = form.save()
        subject = 'Изменение информации в школе'
        message = f'Здравствуйте, {student.name}!\n\nВаши данные в школе были обновлены.'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [student.email])
        return response


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'delete_student.html'
    success_url = '/students/'


class StudentDetailView(DeleteView):
    model = Student
    template_name = 'view_student.html'
    context_object_name = 'student'


class SendEmailView(FormView):
    template_name = 'send_email.html'
    form_class = EmailForm
    success_url = '/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = settings.DEFAULT_FROM_EMAIL
        to_emails = [student.email for student in Student.objects.all()]

        send_mail(subject, message, from_email, to_emails)

        return super().form_valid(form)





