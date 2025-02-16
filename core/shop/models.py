from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField
# Create your models here.


class ProductStatusType(models.IntegerChoices):
    publish = 1, ("نمایش")
    draft = 2, ("عدم نمایش")


class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)
    
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    def  __str__(self):
        return self.title


class ProductModel(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT)
    category = models.ManyToManyField(ProductCategoryModel)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)
    image = models.ImageField(default="/default/product-image.png",upload_to="product/img/")
    description = RichTextField()
    brief_description = models.TextField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=ProductStatusType.choices, default=ProductStatusType.draft.value)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    discount_percent = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        
        
    def get_price(self):
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        
        return int(discounted_amount)
    
    
    def get_show_price(self):
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        
        return "{:,}".format(int(discounted_amount))
    
    def get_show_raw_price(self):
        return "{:,}".format(self.price)
    
    def is_discounted(self):
        return self.discount_percent != 0
    
    def is_published(self):
        return self.status == ProductStatusType.publish.value
    
    def get_images(self):
        return self.images.all()
    
class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="images")
    file = models.ImageField(upload_to="product/extra-img/")
    
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)