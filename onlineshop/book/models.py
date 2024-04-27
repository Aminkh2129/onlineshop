from django.db import models
from django.contrib.auth.models import User


    
class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=5, decimal_places=2)
    image=models.ImageField(upload_to='')
    
    class Meta:
        db_table = 'Product'  



class Category(models.Model):
    type_book=models.CharField(max_length=20)
    author=models.CharField(max_length=25)
    publisher=models.CharField(max_length=20)
    publish_date=models.DateField()
    c_product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='c_product')
    
    class Meta:
        db_table = 'Category'  


class Customer(models.Model):
    Code_meli=models.BigIntegerField(blank=True, null=True , unique=True)
    #First_name=models.CharField(max_length=20)
    #Last_name=models.CharField(max_length=20)
    Address=models.CharField(max_length=200)
    #Email=models.EmailField(unique=True)
    Telephone=models.BigIntegerField(blank=True, null=True , unique=True)
    unit_no=models.BigIntegerField(blank=True, null=True , unique=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')

    class Meta:
        db_table = 'Customer'  




class Order_Item(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')
    quantity=models.PositiveIntegerField(default=1)
    sum_price=models.BigIntegerField(blank=True, null=True , unique=True)

    class Meta:
        db_table = 'Order_Item' 

class Order(models.Model):
    date_order=models.DateTimeField()#
    status_order=models.BooleanField(default=False)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer')
    item=models.ForeignKey(Order_Item,on_delete=models.CASCADE,related_name='item')

    class Meta:
        db_table = 'Order'  
 
