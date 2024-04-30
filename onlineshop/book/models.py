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
    
    PageNumber=[
        ('40','40'),
        ('60','60'),
        ('80','80'),
        ('100','100'),
        ('200','200'),
            ]

    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='',null=True)
    publisher=models.CharField(max_length=20)
    page_number=models.CharField(blank=True, null=True,choices=PageNumber)
    color=models.CharField(max_length=20,choices=COLORS)
    is_active=models.BooleanField(default=True)


    def __str__(self):
            return self.name
    class Meta:
        db_table = 'Notebook'  



class Store(models.Model):
    count=models.BigIntegerField(null=True)
    is_exist=models.BooleanField(default=False)
    product=models.ForeignKey(Notebook,on_delete=models.CASCADE,related_name='product')
    

    def __str__(self):
            return self.product.name
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


    def __str__(self):
            return f"{self.user.first_name}{self.user.last_name} --- {self.Address}"
    
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

    def __str__(self):
            return self.id
    class Meta:
        db_table = 'Order' 

class Order_Item(models.Model):
    notebooks=models.ManyToManyField(Store)
    quantity=models.PositiveIntegerField(default=1)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='item' , null=True )
    

    class Meta:
        db_table = 'Order_Item' 

 
 
