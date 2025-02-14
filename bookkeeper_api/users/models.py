from django.contrib.auth.models import User
from django.db import models

class OrdinaryUser(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    public_username = models.CharField(blank=True, null=False, max_length=10)
