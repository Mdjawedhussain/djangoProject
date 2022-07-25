from django.urls import path
from customer import views

urlpatterns =[
    path("login",views.loginpage),
    path("save",views.save),
    path("loginDo",views.login),
    
]