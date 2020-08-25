from django.contrib.auth.models import AbstractUser
from django.db import models


class myuser(AbstractUser):
    homepage = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    REQUIRED_FIELDS = ['email', 'age']
