from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("product/grid/", views.ShopProductGridView.as_view(), name="shop_product_grid"),
]
