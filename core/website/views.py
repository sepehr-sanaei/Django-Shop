from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import ContactModel
from .forms import ContactModelForm
from django.contrib import messages
# Create your views here.

class IndexView(TemplateView):
    template_name = "website/index.html"

class ContactView(TemplateView):
    template_name = "website/contact.html"
    
class AboutView(TemplateView):
    template_name = "website/About.html"
    
    
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import ContactModel, NewsLetterModel
from .forms import ContactModelForm, NewsLetterModelForm


class ContactModelCreateView(CreateView):
    model = ContactModel
    form_class = ContactModelForm  # The form class that will be used
    template_name = 'website/contact.html'  # The template to render the form
    success_url = reverse_lazy('website:contact')  # Redirect to a success page after form submission
    
    # Handle successful form submission
    def form_valid(self, form):
        # Display success message
        messages.success(self.request, 'ارسال فرم شما با موفقیت انجام شد.☺️')
        return super().form_valid(form)
    
    # Handle unsuccessful form submission
    def form_invalid(self, form):
        # Display error message
        messages.error(self.request, 'مشکلی در ارسال فرم شما پیش آمد لطفا مجددا تلاش کنید😥')
        return super().form_invalid(form)
    
class NewsLetterModelCreateView(CreateView):
    model = NewsLetterModel
    form_class = NewsLetterModelForm
    template_name = 'website/index.html'
    success_url = reverse_lazy('website:index')
    
    def form_valid(self, form):
        # Display success message
        messages.success(self.request, 'ثبت نام شما با موفقیت انجام شد☺️')
        return super().form_valid(form)
    
    # Handle unsuccessful form submission
    def form_invalid(self, form):
        # Display error message
        messages.error(self.request, 'مشکلی در ثبت نام شما پیش آمد لطفا مجددا تلاش کنید😥')
        return super().form_invalid(form)