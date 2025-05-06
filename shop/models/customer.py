from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(
        max_length=254, 
        validators=[MinLengthValidator(8), MaxLengthValidator(254)]
    )
    def isexits(self):
        if Customer.objects.filter(email=self.email).exists():
            return True
        return False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
