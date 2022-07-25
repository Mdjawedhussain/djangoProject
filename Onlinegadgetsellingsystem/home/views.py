from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"home/homepage.html")

def about(request):
    return render(request,"home/about.html")


def item(request):
    return render(request,"home/item.html")

def offer(request):
    return render(request,"home/product.html")

def home(request):
    return render(request,"home/homepage.html")

