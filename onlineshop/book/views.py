from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import TodoSerializers , ASerializers , UserSerializer , BiSerializer
from .models import Todo , a  
from rest_framework.views import APIView
from rest_framework import generics,mixins
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination , LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
