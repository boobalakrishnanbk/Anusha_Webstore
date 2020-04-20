from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Manager_Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farming_location = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    # designation = models.CharField(max_length=30)
    join_date = models.DateField()
    stop_date = models.DateField(null = True)
    locality = models.CharField(max_length=30)
    active = models.BooleanField()

    def __str__(self):
        return self.user.username
