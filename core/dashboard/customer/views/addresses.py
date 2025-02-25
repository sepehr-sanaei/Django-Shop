from django.shortcuts import redirect
from django.views.generic import (
    UpdateView,
    ListView,
    DeleteView,
    CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from django.contrib.auth import views as auth_views
from dashboard.customer.forms import UserAddressForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from order.models import UserAddressModel
from django.contrib import messages

class CustomerAddressListView(LoginRequiredMixin, HasCustomerAccessPermission, ListView):
    template_name = "dashboard/customer/addresses/address-list.html"
    
    
    paginate_by = 10
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = UserAddressModel.objects.filter(user = self.request.user)
        if search_q:=self.request.GET.get('q'):
            queryset = queryset.filter(title__icontains=search_q)  
    
        if order_by:=self.request.GET.get('order_by'):
            queryset = queryset.order_by(order_by)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        
        context["total_amount"] = self.get_queryset().count()
        return context
    
class CustomerAddressCreateView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, CreateView):
    template_name = "dashboard/customer/addresses/address-create.html"
    def get_queryset(self):
        return UserAddressModel.objects.filter(user = self.request.user)
    
    form_class = UserAddressForm
    success_message = "ایجاد آدرس با موفقیت انجام شد"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:customer:address-edit", kwargs={"pk":form.instance.pk}))
    
    def get_success_url(self):
        return reverse_lazy("dashboard:customer:address-list")

class CustomerAddressEditView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/customer/addresses/address-edit.html"
    def get_queryset(self):
        return UserAddressModel.objects.filter(user = self.request.user)
    form_class = UserAddressForm
    success_message = "ویرایش آدرس با موفقیت انجام شد"
    def get_success_url(self):
        return reverse_lazy("dashboard:customer:address-edit", kwargs={"pk":self.get_object().pk})
    
    
class CustomerAddressDeleteView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, DeleteView):
    template_name = "dashboard/customer/addresses/address-delete.html"
    def get_queryset(self):
        return UserAddressModel.objects.filter(user = self.request.user)
    success_message = "آدرس مورد نظر با موفقیت حذف شد"
    success_url = reverse_lazy("dashboard:customer:address-list")