from django import forms
from .models import ContactBusiness

class ContactBusinessForm(forms.ModelForm):
    class Meta:
        model= ContactBusiness
        fields= ('name', 'email', 'message')