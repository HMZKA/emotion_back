from django.shortcuts import render

from rest_framework.permissions import IsAdminUser

from rest_framework import generics

from .serializer import PaymentSerializer

from .models import Payment


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class=PaymentSerializer
    permission_classes = [IsAdminUser]
    
class PaymentUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=PaymentSerializer
    permission_classes = [IsAdminUser]