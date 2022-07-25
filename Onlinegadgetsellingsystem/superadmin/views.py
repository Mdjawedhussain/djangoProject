import imp
from itertools import product
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from customer.models import Customer
from order.models import OrderList
from product.models import Product

# Create your views here.

def dashboard(request):
    
    return render(request, "superadmin/dashboard.html")



def aboutproduct(request):
    product = Product.objects.all()


    return render(request, "superadmin/aboutproduct.html",{'items':product})

    
def register(request):
    if request.method == "POST":
    
        print(request.POST)

        User.objects.create_user(

            first_name =request.POST['firstName'],

            last_name = request.POST['lastName'],

            email = request.POST['email'],

            username = request.POST['username'],

            password = request.POST['password'],



        )

       

    else:

        return render(request,"superadmin/register.html")



    return render(request,"superadmin/register.html")

def loginDo(request):
    if request.method == "POST":
    
        user = authenticate(request,

        username = request.POST['username'],

        password = request.POST['password'])

        print(user)



        if user is not None:

            login(request,user)

            print("login success")

            return redirect("/superadmin/dashboard")

       

        else:

       

            return redirect("/superadmin/loginadmin")

    else:

        return render(request,"superadmin/alogin.html")



def allorder(request):
    order = OrderList.objects.all()
    return render(request,"superadmin/allorder.html",{'order':order})

def allcustomer(request):
    customer = Customer.objects.all()
    return render(request,"superadmin/allcustomer.html",{'customer':customer})


