
from django.db import models

from customer.models import Customer
from product.models import Product

# Create your models here.
class OrderList(models.Model):
    orderId = models.AutoField(auto_created=True,primary_key=True)

    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)

    productId = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=0)




    class Meta:

        db_table= "orderlist"