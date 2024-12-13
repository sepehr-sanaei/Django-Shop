from django.db import models
from accounts.validators import validate_iranian_phone_number
# Create your models here.

class ContactModel(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, validators=[validate_iranian_phone_number], blank=True)
    description = models.TextField()
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        
    def __str__(self):
        return self.email
    
    
class NewsLetterModel(models.Model):
    email = models.EmailField()
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.email