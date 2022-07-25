from django.urls import path
from product import views

urlpatterns =[
    path("product",views.product),
    path("addproduct",views.add),
    path("save",views.saveProduct),
    path("details/<int:id>",views.details),
    path("deleteproduct/<int:id>",views.delete),
    path("editproduct/<int:id>",views.edit),
    path("updateproduct/<int:id>",views.updateproduct),
    
   
    
]