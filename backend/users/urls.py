from django.urls import path



from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('login/',LoginView.as_view(), name='sign_in'),
    path('register/',UserRegisterView.as_view(), name = 'register'),
    path('logout/',UserLogout,name = 'logout')
]