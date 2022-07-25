from django import forms

from order.models import OrderList



class OrderForm(forms.ModelForm):

    class Meta:

        model=OrderList

        fields="__all__"