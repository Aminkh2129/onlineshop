from django.contrib import admin
from .models import Notebook,Customer,Store,Order,Order_Item



# Register your models here.
@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    pass

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Order_Item)
class Order_ItemAdmin(admin.ModelAdmin):
    pass
