from django import forms
from django.forms import ModelForm
from .models import Review 

class UploadForm(ModelForm):
    name = forms.TextInput()
    review = forms.TextInput()
    
    class Meta:
        model = Review
        fields = ['name' , 'review']