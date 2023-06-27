from django.urls import path



from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('login/',LoginView.as_view(), name='login'),
    path('register/',UserRegisterView.as_view(), name = 'register'),
    path('logout/',UserLogout,name = 'logout'),
    path('students/', StudentListView.as_view(), name='teacher_room'),
    path('students/create/', StudentCreateView.as_view(), name='create_student'),
    path('students/update/<int:pk>/', StudentUpdateView.as_view(), name='update_student'),
    path('students/delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
    path('students/view/<int:pk>/', StudentDetailView.as_view(), name='view_student'),
    path('send_email/', SendEmailView.as_view(), name='send_email')

]