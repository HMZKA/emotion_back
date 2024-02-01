from django.urls import path
from .views import CompanyCreateAPIView, CompanyUpdateDestroyAPIView, CompanyListAPIView


urlpatterns = [
    path("", CompanyListAPIView.as_view()),
    path("create/", CompanyCreateAPIView.as_view()),
    path("<int:pk>/", CompanyUpdateDestroyAPIView.as_view()),
]
