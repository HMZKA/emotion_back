from django.urls import path
from .views import UserCreateAPIView, CreateTokenView,ManageUserView


urlpatterns = [
    path("register/", UserCreateAPIView.as_view()),
    path("login/", CreateTokenView.as_view()),
    path("user/", ManageUserView.as_view()),
]
