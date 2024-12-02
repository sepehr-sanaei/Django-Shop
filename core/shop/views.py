from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
                                  
)
from .models import ProductModel, ProductStatusType
# Create your views here.

class ShopProductGridView(ListView):
    template_name = "shop/product_grid.html"
    queryset = ProductModel.objects.filter(status=ProductStatusType.publish.value)