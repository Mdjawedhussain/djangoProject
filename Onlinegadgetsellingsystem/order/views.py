from django.shortcuts import render,redirect

# Create your views here.

from order.forms import OrderForm

# Create your views here.
def save(request):
    order = OrderForm(request.POST)
    order.save()
    return redirect("/product/product")

