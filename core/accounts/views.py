from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from accounts.forms import AuthenticationForm
# Create your views here.


class LoginView(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass

class PasswordResetView(auth_views.PasswordResetView):
    email_template_name = "accounts/password_reset_email.html"
    success_url = reverse_lazy("accounts:password_reset_done")
    
class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy("accounts:password_reset_complete")