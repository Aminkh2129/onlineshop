from rest_framework import serializers
from .models import Notebook,Customer,Store,Order,Order_Item
from django.contrib.auth.models import User



class NotebookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Notebook
        fields='__all__'
