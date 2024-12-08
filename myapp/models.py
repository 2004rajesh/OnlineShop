from django.db import models

# Create your models here.

class Userdata(models.Model):
    username = models.CharField(max_length=200,default="user")
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.username
    
class Product(models.Model):
    
    product_name=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to="product/")
    ogcost=models.IntegerField()
    dcost=models.IntegerField()
    desc=models.TextField()
    
    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user=models.ForeignKey(Userdata,on_delete=models.CASCADE)
    product_item=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.product_item
    

class Checkoutinfo(models.Model):
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.PositiveIntegerField()
    payment=models.CharField(max_length=100,default=None)
    
    def __str__(self):
        return self.email
    
    
   
