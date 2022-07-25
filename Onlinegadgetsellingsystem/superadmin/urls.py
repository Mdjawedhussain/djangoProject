from django.urls import path  
from superadmin import views

urlpatterns = [
    path("registeradmin",views.register),
    path("loginadmin",views.loginDo),
    path("dashboard",views.dashboard),
    path("aboutproduct",views.aboutproduct),
    path("allorder",views.allorder),
    path("allcustomer",views.allcustomer),
    
    
    

]