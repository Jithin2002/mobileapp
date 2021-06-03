from django import forms
from django.forms import ModelForm
from mobileapp.models import Product,Brand

class BrandModelForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields=["brand_name"]
class ProductCreateForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"