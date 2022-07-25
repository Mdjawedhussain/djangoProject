from pyexpat import model
from statistics import mode
from django.db import models
from flask import request

# Create your models here.
class Customer(models.Model):
    customerId = models.AutoField(auto_created=True,primary_key=True)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = "Customer"
        

    @staticmethod

    def get_customer_by_email(email):

        try:

            return Customer.objects.get(email = email)

        except:

            return False