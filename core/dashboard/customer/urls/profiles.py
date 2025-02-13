from django.urls import path
from .. import views


urlpatterns = [
    path('security/edit/', views.CustomerDashboardSecurityEditView.as_view(), name='security-edit'),
    path('profile/edit/', views.CustomerDashboardProfileEditView.as_view(), name='profile-edit'),
    path('profile/image/edit/', views.CustomerDashboardProfileImageEditView.as_view(), name='profile-image-edit'),
]

