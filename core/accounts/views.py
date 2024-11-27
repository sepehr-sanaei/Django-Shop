from django.shortcuts import render
from django.contrib.auth import views as auth_views
from accounts.forms import AuthenticationForm
# Create your views here.


class LoginView(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass