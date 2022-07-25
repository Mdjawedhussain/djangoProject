from django.db import models

# Create your models here.
class Product(models.Model):
    
    productId = models.AutoField(auto_created=True,primary_key=True)

    productName = models.CharField(max_length=200,null=False)

    productPrice = models.CharField(max_length=100, default=0)

    description = models.TextField(max_length=500)

    productImage = models.FileField(upload_to="static/images/products",default="default.jpg")



   



    class Meta:

        db_table = "product"