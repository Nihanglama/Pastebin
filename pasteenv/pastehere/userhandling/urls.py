from django.contrib.auth.urls import path
from . import views
from .views import UserLogin
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',UserLogin.as_view(),name='Login'),
    path('register/',views.register,name='Register'),
    path('logout/',LogoutView.as_view(next_page='Login'),name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='userhandling/reset_form.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='userhandling/message_sent.html'),name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='userhandling/newpassform.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='userhandling/resetdone.html'),name='password_reset_complete'),
]

