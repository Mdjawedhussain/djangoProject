import email
from django.shortcuts import redirect, render
from customer.forms import CustomerForm
from django.contrib import messages

from customer.models import Customer

# Create your views here.

def loginpage(request):
    return render(request,"home/login.html")

def save(request):
    customer = CustomerForm(request.POST)
    customer.save()
    messages.success(request,"User registered Successfully")
    return redirect('/customer/login')

def login(request):
    if request.method == "POST":
        user = request.POST.get('username')
        pasw = request.POST.get('password')

        customer = Customer.get_customer_by_email(user)
        if customer:
            if(pasw == customer.password):
                request.session['email']=customer.email
                request.session['customerId']=customer.customerId
                return redirect("/product/product")
            else:
                messages.success(request,"Password incorrect")

        else:
            messages.success(request, "Invalid user")
    return redirect("/customer/login")


        
        
        


    