from django.shortcuts import redirect, render
from product.forms import ProductForm
from product.models import Product

# Create your views here.
def product(request):
    items={}
    items['product'] = Product.objects.all()
    items['email']=request.session.get('email')
    items['customerId']=request.session.get('customerId')
    

    
    return render(request,"product/product.html",items)

def add(request):
    return render(request,"product/addProduct.html")


def saveProduct(request):
   
    
    data = ProductForm(request.POST,request.FILES)

    data.save()

   

    return redirect("/product/product")

def details(request,id):
    data = {}
    data['product'] =Product.objects.get(productId= id)
    data['email']= request.session.get('email')
    data['customerId'] = request.session.get('customerId')
    return render(request,"product/details.html",data)

def delete(request,id):
    product = Product.objects.get(productId = id)
    product.delete()
    return redirect("/superadmin/aboutproduct")

def edit(request,id):
    data = Product.objects.get(productId= id)
    return render(request,"product/editproduct.html",{'data':data})

def updateproduct(request,id):
    
    
    data=Product.objects.get(productId=id)

    form=ProductForm(request.POST,request.FILES,instance=data)

    form.save()
    return redirect("/superadmin/aboutproduct")