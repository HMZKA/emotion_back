from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializer import CompanySrializer

from .models import Company

# Create your views here.


class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySrializer
    permission_classes=[IsAdminUser]
    
   


class CompanyUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySrializer
    permission_classes = [IsAdminUser]
