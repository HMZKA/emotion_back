from django.urls import path
from .views import CompanyListCreateAPIView, CompanyUpdateDestroyAPIView


urlpatterns = [
    path("", CompanyListCreateAPIView.as_view()),
    path("<int:pk>/", CompanyUpdateDestroyAPIView.as_view()),
]
