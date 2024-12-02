from django.contrib import admin
from .models import ProductCategoryModel, ProductImageModel, ProductModel
# Register your models here.

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "stock", "status", "created_date")
    
    
@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "created_date")
    
    
@admin.register(ProductCategoryModel)
class ProductCategoryModellAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_date")