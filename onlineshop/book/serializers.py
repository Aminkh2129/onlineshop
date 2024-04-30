from rest_framework import serializers
from .models import Notebook,Customer,Store,Order,Order_Item
from django.contrib.auth.models import User



class NotebookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Notebook
        fields='__all__'


class StoreSerializers(serializers.ModelSerializer):
    product=NotebookSerializers(read_only=True , many=True)
    class Meta:
        model=Store
        fields='__all__'