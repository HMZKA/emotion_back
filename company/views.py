from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializer import CompanySrializer

from .models import Company

# Create your views here.


class CompanyCreateAPIView(generics.CreateAPIView):
    serializer_class = CompanySrializer
    permission_classes = [IsAdminUser]


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySrializer


class CompanyUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySrializer
    permission_classes = [IsAdminUser]
