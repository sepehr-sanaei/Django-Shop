from django.shortcuts import redirect
from django.views.generic import (
    UpdateView,
    ListView,
    DeleteView,
    CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.contrib.auth import views as auth_views
from dashboard.admin.forms import AdminPasswordChangeForm, ProductEdit, ProductImageForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from shop.models import ProductModel, ProductCategoryModel, ProductImageModel
from django.contrib import messages
# Create your views here.


class AdminDashboardSecurityEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, auth_views.PasswordChangeView):
    template_name = 'dashboard/admin/profile/security-edit.html'
    form_class = AdminPasswordChangeForm
    success_url = reverse_lazy("dashboard:admin:security-edit")
    success_message = "رمز عبور با موفقیت بروزرسانی شد"
    
    
class AdminProductListView(LoginRequiredMixin, HasAdminAccessPermission, ListView):
    template_name = "dashboard/admin/products/product-list.html"
    
    
    paginate_by = 10
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = ProductModel.objects.all()
        if search_q:=self.request.GET.get('q'):
            queryset = queryset.filter(title__icontains=search_q)  
        if category_id:=self.request.GET.get('category_id'):
            queryset = queryset.filter(category__id=category_id)
        if min_price:=self.request.GET.get('min_price'):
            queryset = queryset.filter(price__gte=min_price)
        if max_price:=self.request.GET.get('max_price'):
            queryset = queryset.filter(price__lte=max_price)
        if max_price:=self.request.GET.get('max_price'):
            queryset = queryset.filter(price__lte=max_price)
        if order_by:=self.request.GET.get('order_by'):
            queryset = queryset.order_by(order_by)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        
        context["total_amount"] = self.get_queryset().count()
        context["categories"] = ProductCategoryModel.objects.all()
        return context
    
class AdminProductCreateView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, CreateView):
    template_name = "dashboard/admin/products/product-create.html"
    queryset = ProductModel.objects.all()
    form_class = ProductEdit
    success_message = "ایجاد محصول با موفقیت انجام شد"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:admin:product-edit", kwargs={"pk":form.instance.pk}))
    
    def get_success_url(self):
        return reverse_lazy("dashboard:admin:product-list")

class AdminProductEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/admin/products/product-edit.html"
    queryset = ProductModel.objects.all()
    form_class = ProductEdit
    success_message = "ویرایش محصول با موفقیت انجام شد"
    def get_success_url(self):
        return reverse_lazy("dashboard:admin:product-edit", kwargs={"pk":self.get_object().pk})
    
    
class AdminProductDeleteView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    template_name = "dashboard/admin/products/product-delete.html"
    queryset = ProductModel.objects.all()
    success_message = "محصول مورد نظر با موفقیت حذف شد"
    success_url = reverse_lazy("dashboard:admin:product-list")
    


class AdminProductAddImageView(LoginRequiredMixin, HasAdminAccessPermission, CreateView):
    http_method_names = ['post']
    form_class = ProductImageForm

    def get_success_url(self):
        return reverse_lazy('dashboard:admin:product-edit', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        product_id = self.kwargs.get('pk')
        try:
            product = ProductModel.objects.get(pk=product_id)
            form.instance.product = product
            form.save()  # Explicitly save the form
            messages.success(self.request, 'تصویر مورد نظر با موفقیت ثبت شد')
            return redirect(self.get_success_url())
        except ProductModel.DoesNotExist:
            messages.error(self.request, 'محصول مورد نظر یافت نشد')
            return redirect(self.get_success_url())


class AdminProductRemoveImageView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    http_method_names = ["post"]
    success_message = "تصویر مورد نظر با موفقیت حذف شد"

    def get_queryset(self):
        return ProductImageModel.objects.filter(product__id=self.kwargs.get('pk'))
    
    def get_object(self, queryset=None):
        return self.get_queryset().get(pk=self.kwargs.get('image_id'))

    def get_success_url(self):
        return reverse_lazy('dashboard:admin:product-edit', kwargs={'pk': self.kwargs.get('pk')})

    def form_invalid(self, form):
        messages.error(
            self.request, 'اشکالی در حذف تصویر رخ داد لطفا مجدد امتحان نمایید')
        return redirect(reverse_lazy('dashboard:admin:product-edit', kwargs={'pk': self.kwargs.get('pk')}))