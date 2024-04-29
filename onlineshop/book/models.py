from django.db import models
from django.contrib.auth.models import User


    
class Notebook(models.Model):

    COLORS=[
        ('white','white'),
        ('black','black'),
        ('red','red'),
        ('blue','blue'),
        ('green','green'),
            ]

    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=5, decimal_places=2)
    image=models.ImageField(upload_to='')
    publisher=models.CharField(max_length=20)
    Telephone=models.BigIntegerField(blank=True, null=True)
    color=models.CharField(max_length=20,choices=COLORS)

    class Meta:
        db_table = 'Notebook'  



class Store(models.Model):
    exist=models.CharField(max_length=20)
    product=models.ForeignKey(Notebook,on_delete=models.CASCADE,related_name='product')
    
    class Meta:
        db_table = 'Category'  


class Customer(models.Model):
    Code_meli=models.BigIntegerField(blank=True, null=True , unique=True)
    #First_name=models.CharField(max_length=20)
    #Last_name=models.CharField(max_length=20)
    Address=models.CharField(max_length=200)
    #Email=models.EmailField(unique=True)
    Telephone=models.CharField(blank=True, null=True , unique=True , max_length=11)
    unit_no=models.IntegerField(blank=True, null=True , unique=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')

    class Meta:
        db_table = 'Customer'  


class Order(models.Model):

    STATUS=[
        ('Accepted','Accepted'),
        ('not confirmed','not confirmed'),
        ('pending','pending'),
    ]
    status_order=models.CharField(default=False,choices=STATUS)
    date_order=models.DateTimeField()#
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer')

    class Meta:
        db_table = 'Order' 

class Order_Item(models.Model):
    notebooks=models.ManyToManyField(Store)
    quantity=models.PositiveIntegerField(default=1)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='item' , null=True )
    

    class Meta:
        db_table = 'Order_Item' 

 
 
