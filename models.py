from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getFileName(instance, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = "%s_%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename)

class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-show,1-hidden")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    quantity=models.IntegerField( null=False, blank=False)
    original_price=models.FloatField( null=False, blank=False)
    selling_price=models.FloatField( null=False, blank=False)

    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-show,1-hidden")
    trending = models.BooleanField(default=False, help_text="0-default,1-trending")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE) 
    Product_qty=models.IntegerField(null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)   

    
    @property
    def total_cost(self):
        return self.Product_qty*self.product.selling_price
      

class Favourite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE) 
    created_at=models.DateTimeField(auto_now_add=True)   


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
