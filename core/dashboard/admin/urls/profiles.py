from django.urls import path
from .. import views



urlpatterns = [
    path('security/edit/', views.AdminDashboardSecurityEditView.as_view(), name='security-edit'),
    path('profile/edit/', views.AdminDashboardProfileEditView.as_view(), name='profile-edit'),
    path('profile/image/edit/', views.AdminDashboardProfileImageEditView.as_view(), name='profile-image-edit'),
]
