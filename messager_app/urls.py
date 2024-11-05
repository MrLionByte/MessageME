from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.Signup.as_view(), name='signup'),
    path('log-in/', views.SignIn.as_view(), name='login'),
    path('messages/', views.MessageView.as_view(), name='message_view'),
]