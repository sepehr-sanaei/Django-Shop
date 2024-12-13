from django import forms
from .models import ContactModel, NewsLetterModel
from accounts.validators import validate_iranian_phone_number

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'description']


    phone_number = forms.CharField(
        max_length=12,
        required=False,
        validators=[validate_iranian_phone_number],
        widget=forms.TextInput(attrs={'placeholder': 'Optional: Enter your phone number'})
    )
    
    
class NewsLetterModelForm(forms.ModelForm):
    class Meta:
        model = NewsLetterModel
        fields = ['email']