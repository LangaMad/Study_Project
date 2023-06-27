from django.shortcuts import render, redirect
from django.views.generic import (
    FormView,
    CreateView,
    TemplateView)
from django.contrib.auth import login,authenticate,logout
from  django.http import HttpResponse
from django.urls import reverse_lazy
from .form import LoginForm, UserRegisterForm
# Create your views here.




class IndexPage(TemplateView):
    template_name = "index.html"


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        phone = data['phone']
        password = data['password']
        user = authenticate(phone=phone, password=password)
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
    success_url = reverse_lazy('teacher_room')



def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')


