from django.urls import path,include
from . import views



urlpatterns = [
    
    path('listproducts/',views.NoteBookListApiView.as_view()),
    path('listproducts/<pk>',views.NoteBookCRDApiView.as_view()),
    path('store/',views.StoreListApiView.as_view()),
    path('store/<pk>',views.StoreCRDApiView.as_view()),
    path('customer/',views.CustomerListApiView.as_view()),
    path('customer/<pk>',views.CustomerCRDApiView.as_view()),
    path('order/',views.OrderListApiView.as_view()),
    path('order/<pk>',views.OrderCRDApiView.as_view()),
    path('orderitem/',views.OrderItemListApiView.as_view()),
    path('orderitem/<pk>',views.OrderItemCRDApiView.as_view()),
]
