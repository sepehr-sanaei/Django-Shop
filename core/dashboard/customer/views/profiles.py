from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from django.contrib.auth import views as auth_views
from dashboard.customer.forms import CustomerPasswordChangeForm, CustomerProfileEditForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from accounts.models import Profile
from django.contrib import messages
# Create your views here.


    
class CustomerDashboardSecurityEditView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, auth_views.PasswordChangeView):
    template_name = 'dashboard/customer/profile/security-edit.html'
    form_class = CustomerPasswordChangeForm
    success_url = reverse_lazy("dashboard:customer:security-edit")
    success_message = "رمز عبور با موفقیت بروزرسانی شد"
    
    
class CustomerDashboardProfileEditView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin,UpdateView):
    template_name = 'dashboard/customer/profile/profile-edit.html'
    form_class = CustomerProfileEditForm
    success_url = reverse_lazy("dashboard:customer:profile-edit")
    success_message = "پروفایل با موفقیت بروزرسانی شد"
    
    def get_object(self, queryset = None):
        return Profile.objects.get(user=self.request.user)
    
    
class CustomerDashboardProfileImageEditView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin,UpdateView):
    http_method_names = ['post']
    model = Profile
    fields = {
        'image'
    }
    success_url = reverse_lazy("dashboard:customer:profile-edit")
    success_message = "تصویر پروفایل با موفقیت بروزرسانی شد"
    
    def get_object(self, queryset = None):
        return Profile.objects.get(user=self.request.user)
    
    def form_invalid(self, form):
        messages.error(self.request, 'بروزرسانی تصویر پروفایل با مشکل مواجه شد مجدد تلاش کنید')
        return redirect(self.success_url)