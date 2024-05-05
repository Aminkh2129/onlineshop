from rest_framework import serializers
from .models import Notebook,Customer,Store,Order,Order_Item
from django.contrib.auth.models import User

class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order_Item
        fields='__all__'


class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model=Store
        fields='__all__'

class NotebookSerializers(serializers.ModelSerializer):
    product=StoreSerializers(read_only=True , many=True)
    notebooks=StoreSerializers(read_only=True , many=True)
    class Meta:
        model=Notebook
        fields=["publisher","name"]

class OrderSerializers(serializers.ModelSerializer):
    item=StoreSerializers(read_only=True , many=True)
    class Meta:
        model=Order
        fields='__all__'

class CustomerSerializers(serializers.ModelSerializer):
    customer=OrderSerializers(read_only=True , many=True)
    class Meta:
        model=Customer
        fields='__all__'

class UserSerializers(serializers.ModelSerializer):
    user=CustomerSerializers(read_only=True , many=True)
    class Meta:
        model=User
        fields='__all__'



