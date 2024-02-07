from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Job
from .serializer import JobSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from django.core.exceptions import ValidationError
from rest_framework import status
# Create your views here.


class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]
    authentication_classes=[TokenAuthentication,SessionAuthentication]


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    # permission_classes = [IsAuthenticated]


class JobUpdateDestoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]
    authentication_classes=[TokenAuthentication,SessionAuthentication]
    
class JobApplyView(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def patch(self, request, *args, **kwargs):
        try:
            job = self.get_object()
            job.apply(request.user)
            return Response({"detail": "Application submitted successfully."}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)