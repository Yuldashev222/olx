from django.db import models
from django.contrib.auth.models import AbstractUser

from api.v1.accounts.validators import validate_phone


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13, blank=True, validators=[validate_phone])
    email = models.EmailField(unique=True)
    balance = models.FloatField()  # kamida 0 bolishi kerak

    # edu1_name
    # edu1_yu
    # edu1_start_date
    # edu1_end_date
    # edu1_now = Bool
    #
    # edu1_name
    # edu1_yu
    # edu1_start_date
    # edu1_end_date
    # edu1_now = Bool
