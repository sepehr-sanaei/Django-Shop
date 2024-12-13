from django.contrib import admin
from .models import ContactModel, NewsLetterModel
# Register your models here.

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "created_date")
    
@admin.register(NewsLetterModel)
class NewsLetterModel(admin.ModelAdmin):
    list_display = ("email", "created_date")