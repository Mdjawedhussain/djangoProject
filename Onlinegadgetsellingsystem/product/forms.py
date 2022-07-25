from django import forms
from product.models import Product
class ProductForm(forms.ModelForm):
    
    class Meta:

        model = Product

        #itme ko every model lai mapping gernae

        fields = "__all__"