from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "admin"

urlpatterns = [
    path('home/', views.AdminDashboardHomeView.as_view(), name='home'),
]
