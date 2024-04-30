from django.urls import path,include
from . import views



urlpatterns = [
    
    path('listproducts/',views.NoteBookListApiView.as_view()),
    path('listproducts/<pk>',views.NoteBookCRDApiView.as_view()),
    path('store/',views.StoreListApiView.as_view()),
]
