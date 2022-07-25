from django.urls import path
from home import views

urlpatterns =[
    path("",views.index,name='home'),
    path("about",views.about),
    path("offer",views.offer),
    path("item",views.item),
    path("home",views.home),
]