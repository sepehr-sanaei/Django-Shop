from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    # send contact form
    path('submit/ticket/', views.ContactModelCreateView.as_view(), name="submit-ticket"),
    # register in newsletter
    path('newsletter/', views.NewsLetterModelCreateView.as_view(), name="newsletter"),
]
