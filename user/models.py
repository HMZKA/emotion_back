import os
import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# Create your models here.
def user_cv_file_path(instance, filename):
    """Generate file path for new recipe cv file"""
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("uploads/cv/", filename)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True, null=False,blank=False)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    cv = models.FileField(null=True, upload_to=user_cv_file_path)

    USERNAME_FIELD = "email"
