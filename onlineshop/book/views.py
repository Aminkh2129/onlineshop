from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import (
    NotebookSerializers,
    StoreSerializers,
    CustomerSerializers,
    OrderSerializers,
    OrderItemSerializers,
)
from .models import Notebook, Customer, Store, Order, Order_Item
from rest_framework.views import APIView
from rest_framework import generics, mixins
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        tags=["Account"],
        operation_summary="filter products",
        operation_description="",
        request_body=NotebookSerializers,
        responses={
            200: openapi.Response("type: ", NotebookSerializers),
            400: "invalid input",
        },
    ),
)
class NoteBookListApiView(generics.ListAPIView):
    # queryset=Notebook.objects.all()
    serializer_class = NotebookSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "color"]

    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "color"]

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["name", "color"]
    ordering = ["name"]

    def get_queryset(self):
        color = self.request.query_params.get("color", "")
        publisher = self.request.query_params.get("publisher", "")
        # pageNumber=self.request.query_params.get('page_number' , '')

        final = Notebook.objects.filter(
            color=color, publisher=publisher, page_number__gt=40
        )
        if not final:
            return Notebook.objects.all()

        return final

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class NoteBookCRDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializers


class StoreListApiView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers


class StoreCRDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers


class CustomerListApiView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

    def get_queryset(self):
        code_meli = self.request.query_params.get("Code_meli", "")
        if not code_meli:
            return Customer.objects.all()
        return Customer.objects.filter(Code_meli=int(code_meli))


class CustomerCRDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class OrderListApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class OrderCRDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class OrderItemListApiView(generics.ListAPIView):
    queryset = Order_Item.objects.all()
    serializer_class = OrderItemSerializers


class OrderItemCRDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order_Item.objects.all()
    serializer_class = OrderItemSerializers
